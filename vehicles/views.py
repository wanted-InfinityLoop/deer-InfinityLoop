import json

from django.http  import JsonResponse
from django.views import View

from vehicles.models import Vehicle, Usage
from core.utils      import login_decorator

class LendKickboardView(View):
    @login_decorator
    def post(self, request):
        try:
            data      = json.loads(request.body)
            deer_name = data["deer_name"]

            Usage.objects.create(
                vehicle = Vehicle.objects.get(deer_name=deer_name),
                user_id = request.user.id
            )

            return JsonResponse({"message": "SUCCESS"}, status=201)

        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)
        
        except Vehicle.DoesNotExist:
            return JsonResponse({"message": "VEHICLE_DOES_NOT_EXIST"}, status=404)
