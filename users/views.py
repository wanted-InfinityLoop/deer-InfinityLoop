import json
import bcrypt
import jwt

from django.views import View
from django.http  import JsonResponse

from users.models    import User
from core.validation import phone_number_validator, email_validator
from my_settings     import MY_SECRET_KEY, ALGORITHM


class SignupView(View):
    def post(self, request):
        try:
            data         = json.loads(request.body)
            email        = data["email"]
            phone_number = data["phone_number"]

            if User.objects.filter(email=email).exists():
                return JsonResponse({"message": "REGISTERED_EMAIL"}, status=400)

            if not email_validator(email):
                return JsonResponse({"message": "INVALID_EMAIL_FORMAT"}, status=400)

            if not phone_number_validator(phone_number):
                return JsonResponse({"message": "INVALID_PHONE_NUMBER_FORMAT"}, status=400)
            
            User.objects.create(
                name        =data["name"],
                email       =email,
                phone_number=bcrypt.hashpw(phone_number.encode("utf-8"), bcrypt.gensalt()).decode("utf-8"),
            )

            return JsonResponse({"message": "Success"}, status=201)

        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)


class SigninView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            if not User.objects.filter(email=data["email"]).exists():
                return JsonResponse({"message": "INVALID_USER"}, status=401)
            
            user = User.objects.get(email=data["email"])

            if not bcrypt.checkpw(data["phone_number"].encode("utf-8"), user.phone_number.encode("utf-8")):
                return JsonResponse({"message": "INVALID_USER"}, status=401)

            access_token = jwt.encode({"user_id": str(user.id)}, MY_SECRET_KEY, ALGORITHM)

            return JsonResponse({"message": "Success", "token": access_token}, status=200) 

        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)
