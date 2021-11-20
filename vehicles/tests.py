import json
import jwt
import bcrypt
from datetime import datetime

from django.test             import TestCase, Client
from django.contrib.gis.geos import Point, Polygon, MultiPoint

from users.models    import User, Role
from vehicles.models import Vehicle, Usage
from areas.models    import ServiceArea, ParkingArea, ForbiddenArea
from charges.models  import Unit, Type, DiscountOrPenalties, Charge
from my_settings     import ALGORITHM, MY_SECRET_KEY


class VehicleViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        
        ServiceArea.objects.create(
            id=1,
            boundary=Polygon( ((0.0, 0.0), (0.0, 50.0), (50.0, 50.0), (50.0, 0.0), (0.0,0.0)) ),
            center=Point(5, 23),
            border_coords=MultiPoint(Point(0, 0), Point(1, 1))
            )
        
        Vehicle.objects.create(
            id=1,
            deer_name="씽씽이",
            service_area=ServiceArea.objects.get(id=1)
        )
        
        user1 = User.objects.create(
            name='이광수',
            email='admin1@dgmail.com',
            phone_number=bcrypt.hashpw("010-1111-2222".encode("utf-8"), bcrypt.gensalt()).decode("utf-8"),
            role=Role.objects.create(name="ADMIN")
            )
        
        self.access_token1 = jwt.encode(
            {"user_id": str(user1.id)}, MY_SECRET_KEY, ALGORITHM
        )

    def tearDown(self):
        ServiceArea.objects.all().delete()
        Vehicle.objects.all().delete()
        User.objects.all().delete()
        Usage.objects.all().delete()
        
    def test_post_usage_success(self):
        header = {"HTTP_Authorization": f"Bearer {self.access_token1}"}
        
        data = {
            "deer_name" : "씽씽이",
            }
        
        response = self.client.post("/vehicles/lend",json.dumps(data),
                                    content_type="application/json", **header)
        
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(),{"message": "SUCCESS"})
        
    def test_post_usage_fail_key_error(self):
        header = {"HTTP_Authorization": f"Bearer {self.access_token1}"}
        
        data = {
            "deer_nam" : "씽씽이",
            }
        
        response = self.client.post("/vehicles/lend",json.dumps(data),
                                    content_type="application/json", **header)
        
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(),{"message": "KEY_ERROR"})

    def test_post_usage_fail_vehicle_doesNotExist(self):
        header = {"HTTP_Authorization": f"Bearer {self.access_token1}"}
        
        data = {
            "deer_name" : "쌩쌩이",
            }
        
        response = self.client.post("/vehicles/lend",json.dumps(data),
                                    content_type="application/json", **header)
        
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(),{"message": "VEHICLE_DOES_NOT_EXIST"})


class ReturnKickboardViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        with open('map.geojson', 'r', encoding='utf-8') as geojson:
            geo_data = json.load(geojson)
        
        features = geo_data["features"]

        for feat in features:
            if feat["properties"]["title"]=="ServiceArea":
                service_area   = Polygon(feat["geometry"]["coordinates"][0])
                service_coords = MultiPoint([Point(x,y) for x,y in service_area[0][:-1]])
            
            elif feat["properties"]["title"]=="ForbiddenArea":
                forbidden_area   = Polygon(feat["geometry"]["coordinates"][0])
                forbidden_coords = MultiPoint([Point(x,y) for x,y in forbidden_area[0][:-1]])
            
        user = User.objects.create(
            email="abc@gmail.com",
            phone_number = bcrypt.hashpw("010-2345-3544".encode("utf-8"), bcrypt.gensalt()).decode("utf-8"),
            name="스폰지밥",
            role=Role.objects.create(name="ADMIN")
        )

        self.access_token = jwt.encode(
            {"user_id": str(user.id)}, MY_SECRET_KEY, ALGORITHM
        )

        Type.objects.create(id=1, name="discount")
        Type.objects.create(id=2, name="penalty")

        unit1 = Unit.objects.create(name="%")
        unit2 = Unit.objects.create(name="원")

        self.e1 = DiscountOrPenalties.objects.create(
            id='P-P-1', 
            number=6000, 
            description="반납 금지 지역 반납", 
            unit=unit2,
            type_id=2
        ),
        self.e2 = DiscountOrPenalties.objects.create(
            id='P-A-1', 
            number=10, 
            description="지역 이탈 반납", 
            unit=unit1,
            type_id=2
        ),
        self.e3 = DiscountOrPenalties.objects.create(
            id='D-P-1', 
            number=30, 
            description="파킹존 반납",
            unit=unit1,
            type_id=1
        )

        charge = Charge.objects.create(rental_charge = 790, additional_charge = 150)

        self.srvc = ServiceArea.objects.create(
            boundary=service_area, 
            center=service_area.centroid, 
            border_coords=service_coords,
            charge=charge
        )

        ForbiddenArea.objects.create(
            boundary=forbidden_area, 
            border_coords = forbidden_coords, 
            service_area=self.srvc
        )
        
        ParkingArea.objects.create(
            center_lat=36.1234,
            center_lng=127.1234,
            radius=100.0,
            service_area=self.srvc
        )

        self.vehicle_1 = Vehicle.objects.create(
            deer_name="ZRC-PFT",
            service_area=self.srvc
        )

        self.vehicle_2 = Vehicle.objects.create(
            deer_name="BPR-SCS",
            service_area=self.srvc
        )

        Usage.objects.create(
            vehicle=self.vehicle_1,
            start_at=datetime(2021,11,21,18,0),
            user=user
        )

        self.srvc.discount_or_penalties.add(*[self.e1, self.e2, self.e3])

    def tearDown(self):
        self.srvc.discount_or_penalties.remove(self.e1)
        self.srvc.discount_or_penalties.remove(self.e2)
        self.srvc.discount_or_penalties.remove(self.e3)
        User.objects.all().delete()
        Role.objects.all().delete()
        DiscountOrPenalties.objects.all().delete()
        Unit.objects.all().delete()
        Type.objects.all().delete()
        Charge.objects.all().delete()
        Vehicle.objects.all().delete()
        ParkingArea.objects.all().delete()
        ServiceArea.objects.all().delete()
        ForbiddenArea.objects.all().delete()

    def test_return_kickboard_view_patch_success(self):
        header = {'HTTP_Authorization': f"Bearer {self.access_token}"}
        data   = {
            "end_lat": 37.4753,
            "end_lng": 126.8719
        }

        response = self.client.patch(
            f'/vehicles/return/{self.vehicle_1.id}', json.dumps(data), content_type="application/json", **header
        )

        self.assertEqual(response.json(), {"message": "CREATED"})
        self.assertEqual(response.status_code, 201)

    def test_return_kickboard_view_patch_value_error(self):
        header = {'HTTP_Authorization': f"Bearer {self.access_token}"}
        data   = {
            "end_lat": 'a',
            "end_lng": 126.8719
        }

        response = self.client.patch(
            f'/vehicles/return/{self.vehicle_1.id}', json.dumps(data), content_type="application/json", **header
        )

        self.assertEqual(response.json(), {"message": "INVALID_VALUES"})
        self.assertEqual(response.status_code, 400)

    def test_return_kickboard_view_patch_usage_does_not_exists(self):
        header = {'HTTP_Authorization': f"Bearer {self.access_token}"}
        data   = {
            "end_lat": 37.4753,
            "end_lng": 126.8719
        }

        response = self.client.patch(
            f'/vehicles/return/{self.vehicle_2.id}', json.dumps(data), content_type="application/json", **header
        )

        self.assertEqual(response.json(), {"message": "HISTORY_DOES_NOT_EXIST"})
        self.assertEqual(response.status_code, 404)

    def test_return_kickboard_view_patch_key_error(self):
        header = {'HTTP_Authorization': f"Bearer {self.access_token}"}
        data   = {
            "this_key_is_so_strange": 37.4753,
            "end_lng": 126.8719
        }

        response = self.client.patch(
            f'/vehicles/return/{self.vehicle_2.id}', json.dumps(data), content_type="application/json", **header
        )

        self.assertEqual(response.json(), {"message": "KEY_ERROR"})
        self.assertEqual(response.status_code, 400)

    def test_return_kickboard_view_patch_usage_validation_error(self):
        header = {'HTTP_Authorization': f"Bearer {self.access_token}"}
        data   = {
            "end_lat": 37.4753,
            "end_lng": 126.8719
        }

        response = self.client.patch(
            '/vehicles/return/134', json.dumps(data), content_type="application/json", **header
        )

        self.assertEqual(response.json(), {"message": "UUID_FORMAT_ERROR"})
        self.assertEqual(response.status_code, 400)
