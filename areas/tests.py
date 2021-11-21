import bcrypt
import json
import jwt

from django.test             import TestCase, Client
from django.contrib.gis.geos import Point, Polygon, MultiPoint

from users.models   import User, Role
from areas.models   import ServiceArea
from charges.models import Unit, Type, DiscountOrPenalties, Charge
from my_settings    import MY_SECRET_KEY, ALGORITHM


class AreaServiceTest(TestCase):
    def setUp(self):
        self.client = Client()

        Charge.objects.create(id=1, rental_charge=3000, additional_charge=1000)

        Unit.objects.create(id=1, name="%")

        Type.objects.create(id=1, name="DISCOUNT")

        Role.objects.bulk_create([Role(id=1, name="관리자"), Role(id=2, name="사용자")])

        user1 = User.objects.create(
            name        ="테스트어드민유저1",
            email       ="test2@server.com",
            phone_number=bcrypt.hashpw("010-1111-2222".encode("utf-8"), bcrypt.gensalt()).decode("utf-8"),
            role_id     =1
        )

        user2 = User.objects.create(
            name        ="테스트커스텀유저1",
            email       ="test1@server.com",
            phone_number=bcrypt.hashpw("010-1111-2222".encode("utf-8"), bcrypt.gensalt()).decode("utf-8"),
            role_id     =2
        )

        self.admin_token = jwt.encode(
            {"user_id": str(user1.id)}, MY_SECRET_KEY, ALGORITHM
        )

        self.customer_token = jwt.encode(
            {"user_id": str(user2.id)}, MY_SECRET_KEY, ALGORITHM
        )

        self.discount_or_penalties = DiscountOrPenalties.objects.create(
            id         ="D-P-1",
            number     =10,
            description="테스트 할인율1",
            unit_id    =1,
            type_id    =1
        )

        DiscountOrPenalties.objects.create(
            id         ="D-P-2",
            number     =10,
            description="테스트 할인율2",
            unit_id    =1,
            type_id    =1
        )

        self.service_area = ServiceArea.objects.create(
            id           =1,
            name         ="강남",
            boundary     =Polygon(((0.0, 0.0), (0.0, 50.0), (50.0, 50.0), (50.0, 0.0), (0.0, 0.0))),
            center       =Point(10,10),
            border_coords=MultiPoint(Point(0, 0), Point(1, 1)),
            charge_id    =1,
            )

        self.service_area.discount_or_penalties.add(self.discount_or_penalties)

    def tearDown(self):
        ServiceArea.objects.all().delete()
        DiscountOrPenalties.objects.all().delete()
        User.objects.all().delete()
        Role.objects.all().delete()
        Type.objects.all().delete()
        Unit.objects.all().delete()
        Charge.objects.all().delete()

    def test_post_area_event_success(self):
        header = {"HTTP_Authorization": f"Bearer {self.admin_token}"}

        data = {"code": "D-P-2", "region": "강남"}

        response = self.client.post(
            "/areas/service", json.dumps(data), content_type="application/json", **header
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "SUCCESS"})

    def test_post_area_event_unauthorized_error(self):
        header = {"HTTP_Authorization": f"Bearer {self.customer_token}"}

        data = {"code": "D-P-2", "region": "강남"}

        response = self.client.post(
            "/areas/service", json.dumps(data), content_type="application/json", **header
        )

        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json(), {"message": "UNAUTHORIZED"})

    def test_post_area_event_invalid_code(self):
        header = {"HTTP_Authorization": f"Bearer {self.admin_token}"}

        data = {"code": "O-P-2", "region": "강남"}

        response = self.client.post(
           "/areas/service", json.dumps(data), content_type="application/json", **header
        )

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {"message": "CODE_NOT_EXIST"})

    def test_post_area_event_invalid_region(self):
        header = {"HTTP_Authorization": f"Bearer {self.admin_token}"}

        data = {"code": "D-P-2", "region": "신촌"}

        response = self.client.post(
           "/areas/service", json.dumps(data), content_type="application/json", **header
        )

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {"message": "RESION_NOT_EXIST"})
        
    def test_post_area_event_already_exist_code(self):
        header = {"HTTP_Authorization": f"Bearer {self.admin_token}"}

        data = {"code": "D-P-1", "region": "강남"}

        response = self.client.post(
            "/areas/service", json.dumps(data), content_type="application/json", **header
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"message": "CODE_ALREADY_EXIST"})

    def test_post_area_event_key_error(self):
        header = {"HTTP_Authorization": f"Bearer {self.admin_token}"}

        data = {"codes": "D-P-2", "region": "강남"}

        response = self.client.post(
            "/areas/service", json.dumps(data), content_type="application/json", **header
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"message": "KEY_ERROR"})

    def test_delete_area_event_success(self):
        header = {"HTTP_Authorization": f"Bearer {self.admin_token}"}

        data = {"code": "D-P-1", "region": "강남"}

        response = self.client.delete(
            "/areas/service", json.dumps(data), content_type="application/json", **header
        )

        self.assertEqual(response.json(), {"message": "D-P-1 is removed"})
        self.assertEqual(response.status_code, 200)

    def test_delete_area_event_unauthorized_error(self):
        header = {"HTTP_Authorization": f"Bearer {self.customer_token}"}

        data = {"code": "D-P-1", "region": "강남"}

        response = self.client.delete(
            "/areas/service", json.dumps(data), content_type="application/json", **header
        )

        self.assertEqual(response.json(), {"message": "UNAUTHORIZED"})
        self.assertEqual(response.status_code, 401)

    def test_delete_area_event_invalid_code(self):
        header = {"HTTP_Authorization": f"Bearer {self.admin_token}"}

        data = {"code": "D-P-2", "region": "강남"}

        response = self.client.delete(
            "/areas/service", json.dumps(data), content_type="application/json", **header
        )

        self.assertEqual(response.json(), {"message": "NOT_FOUND_DP_THIS_SERVICE_AREA"})
        self.assertEqual(response.status_code, 404)

    def test_delete_area_event_invalid_region(self):
        header = {"HTTP_Authorization": f"Bearer {self.admin_token}"}

        data = {"code": "D-P-1", "region": "신촌"}

        response = self.client.delete(
            "/areas/service", json.dumps(data), content_type="application/json", **header
        )

        self.assertEqual(response.json(), {"message": "SERVICE_AREA_DOES_NOT_EXIST"})
        self.assertEqual(response.status_code, 404)

    def test_delete_area_event_key_error(self):
        header = {"HTTP_Authorization": f"Bearer {self.admin_token}"}

        data = {"region": "강남"}

        response = self.client.delete(
            "/areas/service", json.dumps(data), content_type="application/json", **header
        )

        self.assertEqual(response.json(), {"message": "KEY_ERROR"})
        self.assertEqual(response.status_code, 400)
