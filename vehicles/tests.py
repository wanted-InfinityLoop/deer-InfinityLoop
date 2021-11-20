import json
import jwt
import bcrypt

from django.test             import TestCase, Client
from django.contrib.gis.geos import Point, Polygon, MultiPoint

from users.models    import User, Role
from vehicles.models import Vehicle, Usage
from areas.models    import ServiceArea
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
