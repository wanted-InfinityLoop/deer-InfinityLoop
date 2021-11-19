import json
import bcrypt
import jwt

from django.test import TestCase, Client

from users.models import User, Role
from my_settings import MY_SECRET_KEY, ALGORITHM


class SignupViewTest(TestCase):
    def setUp(self):
        self.client = Client()

        Role.objects.bulk_create([Role(id=1, name="관리자"), Role(id=2, name="사용자")])

        User.objects.create(
            name        ="테스트유저2",
            email       ="test2@server.com",
            phone_number="010-3333-4444",
        )

    def tearDown(self):
        User.objects.all().delete()
        Role.objects.all().delete()

    def test_post_signup_success(self):
        data = {
            "name"        : "테스트유저",
            "email"       : "test@server.com",
            "phone_number": "010-1111-2222",
        }

        response = self.client.post(
            "/users/signup", json.dumps(data), content_type="application/json"
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {"message": "Success"})

    def test_post_signup_duplicated_email(self):
        data = {
            "name"        : "테스트유저",
            "email"       : "test2@server.com",
            "phone_number": "010-1111-2222",
        }

        response = self.client.post(
            "/users/signup", json.dumps(data), content_type="application/json"
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"message": "REGISTERED_EMAIL"})

    def test_post_signup_email_format_error(self):
        data = {
            "name"        : "테스트유저",
            "email"       : "testserver.com",
            "phone_number": "010-1111-2222",
        }

        response = self.client.post(
            "/users/signup", json.dumps(data), content_type="application/json"
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"message": "INVALID_EMAIL_FORMAT"})

    def test_post_signup_phone_number_format_error(self):
        data = {
            "name"        : "테스트유저",
            "email"       : "test@server.com",
            "phone_number": "01011112222",
        }

        response = self.client.post(
            "/users/signup", json.dumps(data), content_type="application/json"
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"message": "INVALID_PHONE_NUMBER_FORMAT"})

    def test_post_signup_key_error(self):
        data = {
            "email"       : "test@server.com",
            "phone_number": "010-1111-2222",
        }

        response = self.client.post(
            "/users/signup", json.dumps(data), content_type="application/json"
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"message": "KEY_ERROR"})


class SigninViewTest(TestCase):
    def setUp(self):
        self.cilent = Client()

        Role.objects.bulk_create([Role(id=1, name="관리자"), Role(id=2, name="사용자")])

        user1 = User.objects.create(
            name        ="테스트유저1",
            email       ="test1@server.com",
            phone_number=bcrypt.hashpw("010-1111-2222".encode("utf-8"), bcrypt.gensalt()).decode("utf-8"),
        )

        self.access_token1 = jwt.encode(
            {"user_id": str(user1.id)}, MY_SECRET_KEY, ALGORITHM
        )

    def tearDown(self):
        User.objects.all().delete()
        Role.objects.all().delete()

    def test_post_signin_success(self):
        data = {"email": "test1@server.com", "phone_number": "010-1111-2222"}

        response = self.client.post(
            "/users/signin", json.dumps(data), content_type="application/json"
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Success", "token": self.access_token1})

    def test_post_signin_invalid_user_email(self):
        data = {"email": "test3@server.com", "phone_number": "010-1111-2222"}

        response = self.client.post(
            "/users/signin", json.dumps(data), content_type="application/json"
        )

        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json(), {"message": "INVALID_USER"})

    def test_post_signin_invalid_user_phone_number(self):
        data = {"email": "test1@server.com", "phone_number": "010-3333-4444"}

        response = self.client.post(
            "/users/signin", json.dumps(data), content_type="application/json"
        )

        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json(), {"message": "INVALID_USER"})

    def test_post_signin_key_error(self):
        data = {"mail": "test1@server.com", "phone_number": "010-3333-4444"}

        response = self.client.post(
            "/users/signin", json.dumps(data), content_type="application/json"
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"message": "KEY_ERROR"})
