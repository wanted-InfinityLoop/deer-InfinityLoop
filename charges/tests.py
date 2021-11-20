import bcrypt
import json
import jwt

from django.test import TestCase, Client

from users.models   import User, Role
from charges.models import Unit, Type, DiscountOrPenalties

from my_settings import MY_SECRET_KEY, ALGORITHM


class DiscountViewTest(TestCase):
    def setUp(self):
        self.client = Client()

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
            phone_number=bcrypt.hashpw("010-1111-3333".encode("utf-8"), bcrypt.gensalt()).decode("utf-8"),
            role_id     =2
        )

        self.admin_token = jwt.encode(
            {"user_id": str(user1.id)}, MY_SECRET_KEY, ALGORITHM
        )

        self.customer_token = jwt.encode(
            {"user_id": str(user2.id)}, MY_SECRET_KEY, ALGORITHM
        )

    def tearDown(self):
        DiscountOrPenalties.objects.all().delete()
        User.objects.all().delete()
        Role.objects.all().delete()
        Type.objects.all().delete()
        Unit.objects.all().delete()

    def test_post_discount_success(self):
        header = {"HTTP_Authorization": f"Bearer {self.admin_token}"}

        data = {
            "code"       : "D-P-1",
            "number"     : 10,
            "description": "올바른 주차장에 주차했을시 할인율"
        }

        response = self.client.post(
            "/charges/discount", json.dumps(data), content_type="application/json", **header
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {"message": "SUCCESS"})

    def test_post_discount_unauthorized_error(self):
        header = {"HTTP_Authorization": f"Bearer {self.customer_token}"}

        data = {
            "code"       : "D-P-1",
            "number"     : 10,
            "description": "올바른 주차장에 주차했을시 할인율"
        }

        response = self.client.post(
            "/charges/discount", json.dumps(data), content_type="application/json", **header
        )

        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json(), {"message": "UNAUTHORIZED"})

    def test_post_discount_invalid_code(self):
        header = {"HTTP_Authorization": f"Bearer {self.admin_token}"}

        data = {
            "code"       : "A-P-1",
            "number"     : 10,
            "description": "올바른 주차장에 주차했을시 할인율"
        }

        response = self.client.post(
            "/charges/discount", json.dumps(data), content_type="application/json", **header
        )

        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json(), {"message": "INVALID_CODE_FORMAT"})

    def test_post_discount_type_error(self):
        header = {"HTTP_Authorization": f"Bearer {self.admin_token}"}

        data = {
            "code"       : 9,
            "number"     : 10,
            "description": "올바른 주차장에 주차했을시 할인율"
        }

        response = self.client.post(
            "/charges/discount", json.dumps(data), content_type="application/json", **header
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"message": "TYPE_ERROR"})

    def test_post_discount_key_error(self):
        header = {"HTTP_Authorization": f"Bearer {self.admin_token}"}

        data = {"code": "D-P-3", "description": "올바른 주차장에 주차했을시 할인율"}

        response = self.client.post(
            "/charges/discount", json.dumps(data), content_type="application/json", **header
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"message": "KEY_ERROR"})

    def test_post_discount_value_error(self):
        header = {"HTTP_Authorization": f"Bearer {self.admin_token}"}

        data = {
            "code"       : "D-P-1",
            "number"     : "",
            "description": "올바른 주차장에 주차했을시 할인율"
        }

        response = self.client.post(
            "/charges/discount", json.dumps(data), content_type="application/json", **header
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"message": "VALUE_ERROR"})
