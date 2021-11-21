import json

from django.views            import View
from django.http             import JsonResponse
from django.db               import transaction
from django.core.exceptions  import ValidationError
from django.contrib.gis.geos import Polygon, Point, MultiPoint

from users.models   import Role
from areas.models   import ServiceArea
from charges.models import Charge, DiscountOrPenalties
from core.utils     import login_decorator


class ServiceAreaView(View):
    @login_decorator
    def post(self, request, charge_id):
        try:
            if request.user.role_id != Role.Type.ADMIN.value:
                return JsonResponse({"message": "UNAUTHORIZED"}, status=401)
            data = json.loads(request.body)
            point_list = []

            with transaction.atomic():
                charge = Charge.objects.select_for_update().get(id=charge_id)

                for point in data["boundary"]:
                    point_list.append(Point(point, srid=4326))

                if ServiceArea.objects.filter(name=data["name"]).exists():
                    return JsonResponse({"message": f"{data['name']}_ALREADY_REGISTERED"}, status=400)

                service_area = ServiceArea.objects.create(
                    name         =data["name"],
                    boundary     =Polygon(point_list, srid=4326),
                    center       =Point(data["center"], srid=4326),
                    border_coords=MultiPoint(point_list[: len(point_list)], srid=4326),
                    charge       =charge,
                )

                if data["code"]:
                    for code in data["code"]:
                        dp_object = DiscountOrPenalties.objects.get(id=code)
                        service_area.discount_or_penalties.add(dp_object)
                        service_area.save()

            return JsonResponse({"message": f"{service_area.name} has created!"}, status=201)

        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)

        except ValidationError:
            return JsonResponse({"message": "UUID_FORMAT_ERROR"}, status=400)

        except Charge.DoesNotExist:
            return JsonResponse({"message": "CHARGE_DOES_NOT_EXIST"}, status=404)

        except DiscountOrPenalties.DoesNotExist:
            return JsonResponse({"message": "DISCOUNT_OR_PENALTIES_DOES_NOT_EXIST"}, status=404)


class ServiceAreaDPView(View):
    @login_decorator
    def post(self, request):
        try:
            if request.user.role_id != Role.Type.ADMIN.value:
                return JsonResponse({"message": "UNAUTHORIZED"}, status=401)

            data   = json.loads(request.body)

            area = ServiceArea.objects.get(name=data["region"])
            
            if area.discount_or_penalties.filter(id=data["code"]).exists():
                return JsonResponse({"message": "CODE_ALREADY_EXIST"}, status=400)
            
            charge_event = DiscountOrPenalties.objects.get(id=data["code"])

            area.discount_or_penalties.add(charge_event)

            return JsonResponse({"message": "SUCCESS"}, status=200)

        except DiscountOrPenalties.DoesNotExist:
            return JsonResponse({"message": "CODE_NOT_EXIST"}, status=404) 

        except ServiceArea.DoesNotExist:
            return JsonResponse({"message": "RESION_NOT_EXIST"}, status=404) 
        
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)
