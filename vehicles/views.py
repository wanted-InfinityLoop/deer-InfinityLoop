import json
from datetime  import datetime
from haversine import haversine

from django.http             import JsonResponse
from django.views            import View
from django.core.exceptions  import ValidationError
from django.contrib.gis.geos import Point

from vehicles.models import Vehicle, Usage
from core.utils      import login_decorator


class LendKickboardView(View):
    @login_decorator
    def post(self, request, vehicle_id):
        try:
            vehicle_id = vehicle_id

            if Usage.objects.filter(vehicle_id=vehicle_id, end_at__isnull=True).exists():
                return JsonResponse({"message": "VEHICLE_ALREADY_IN_USE"}, status=409)

            Usage.objects.create(
                vehicle = Vehicle.objects.get(id=vehicle_id),
                user_id = request.user.id
            )

            return JsonResponse({"message": "SUCCESS"}, status=201)
        
        except Vehicle.DoesNotExist:
            return JsonResponse({"message": "VEHICLE_DOES_NOT_EXIST"}, status=404)

        except ValidationError:
            return JsonResponse({"message": "UUID_FORMAT_ERROR"}, status=400)


class ReturnKickboardView(View):
    @login_decorator
    def patch(self, request, vehicle_id):
        try:
            end_at = datetime.now()

            data = json.loads(request.body)
            
            user_id = request.user.id

            end_lat    = data["end_lat"]
            end_lng    = data["end_lng"]
            vehicle_id = vehicle_id

            if not (isinstance(end_lat, float) and isinstance(end_lng, float)):
                return JsonResponse({"message": "INVALID_VALUES"}, status=400)

            usage_histories = Usage.objects.filter(
                user_id=user_id, vehicle_id=vehicle_id, end_at__isnull=True
                ).select_related('vehicle__service_area__charge') 

            if not usage_histories.exists():
                return JsonResponse({"message": "HISTORY_DOES_NOT_EXIST"}, status=404)

            usage_history      = usage_histories.get(user_id = user_id, vehicle_id = vehicle_id)
            start_at           = usage_history.start_at
            area_object        = usage_history.vehicle.service_area
            total_play_time    = (end_at - start_at).seconds/60
            is_within_1_minute = total_play_time <= 1

            if is_within_1_minute:
                usage_history.end_lat       = end_lat
                usage_history.end_lng       = end_lng
                usage_history.end_at        = end_at

                usage_history.save()

                return JsonResponse({"message": "UPDATED"}, status=201)

            return_point    = Point(end_lng, end_lat, srid=4326)
            is_in_area      = area_object.boundary.contains(return_point)
            is_forbidden    = any(
                forbidden_zone.boundary.contains(return_point)
                for forbidden_zone in area_object.forbiddenarea_set.all())
            is_parking_zone = any(
                haversine(
                    return_point, Point(
                        float(parking_point.center_lat), float(parking_point.center_lng), srid=4326
                    ), unit='m') <= parking_point.radius
                for parking_point in area_object.parkingarea_set.all()
            )
            default_charge  = area_object.charge.rental_charge
            charge_per_min  = area_object.charge.additional_charge
            total_charge    = round(total_play_time * charge_per_min)

            if not is_in_area:
                boundary = area_object.boundary
                boundary.transform(5174)
                return_point.transform(5174)

                penalty = area_object.discount_or_penalties.get_or_none(id='P-A-1', type=2)
                dist    = boundary.distance(return_point)

                if penalty:
                    if penalty.unit.name=='%':
                        total_charge += dist * penalty.number * 0.01
                    
                    else:
                        total_charge += penalty.number

            if is_forbidden:
                penalty = area_object.discount_or_penalties.get_or_none(id='P-F-1', type=2)
                
                if penalty:
                    if penalty.unit.name=='%':
                        total_charge += total_charge * penalty.number * 0.01

                    else:
                        total_charge += penalty.number

            if is_parking_zone:
                discount = area_object.discount_or_penalties.get_or_none(id='D-P-1', type=1)

                if discount:
                    if discount.unit.name=='%':
                        total_charge -= total_charge * discount.number * 0.01

                    else:
                        total_charge -= discount.number

            usage_history.end_lat       = end_lat
            usage_history.end_lng       = end_lng
            usage_history.end_at        = end_at
            usage_history.charge_amount = total_charge + default_charge if total_charge > 0 else 0

            usage_history.save()

            return JsonResponse({"message": "UPDATED"}, status=201)
        
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)

        except ValidationError:
            return JsonResponse({"message": "UUID_FORMAT_ERROR"}, status=400)
