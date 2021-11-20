import json

from django.http     import JsonResponse
from django.views    import View
from django.db.utils import IntegrityError

from users.models    import Role
from charges.models  import Unit, Type, DiscountOrPenalties
from core.utils      import login_decorator
from core.validation import code_validator


class DiscountView(View):
    @login_decorator
    def post(self, request):
        try:
            if request.user.role_id != Role.Type.ADMIN.value:
                return JsonResponse({"message": "UNAUTHORIZED"}, status=401)

            data = json.loads(request.body)

            if not data["code"] or not data["number"] or not data["description"]:
                return JsonResponse({"message": "VALUE_ERROR"}, status=400)

            if not code_validator("D", data["code"]):
                return JsonResponse({"message": "INVALID_CODE_FORMAT"}, status=401)

            DiscountOrPenalties.objects.create(
                id         =data["code"],
                number     =data["number"],
                description=data["description"],
                unit       =Unit.objects.get(name="%"),
                type_id    =Type.Type.DISCOUNT.value
            )

            return JsonResponse({"message": "SUCCESS"}, status=201)

        except IntegrityError:
            return JsonResponse({"message": "DUPLICATE_DATA"}, status=409)

        except TypeError:
            return JsonResponse({"message": "TYPE_ERROR"}, status=400)

        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)

        except Unit.DoesNotExist:
            return JsonResponse({"message": "UNIT_NOT_EXIST"}, status=404) 
    
    @login_decorator
    def put(self, request, discount_id):
        try: 
            if request.user.role_id != Role.Type.ADMIN.value:
                return JsonResponse({"message": "UNAUTHORIZED"}, status = 401)
            
            data = json.loads(request.body)

            discount_entity = DiscountOrPenalties.objects.get(id=discount_id)

            if data["number"]:
                discount_entity.number = data["number"]

            if data["description"]:
                discount_entity.description = data["description"]

            discount_entity.save()
            
            return JsonResponse({"result" : {"discount_rate" : discount_entity.number,
                "description" : discount_entity.description}}, status=200)

        except DiscountOrPenalties.DoesNotExist:
            return JsonResponse({"message": "DISCOUNT_DOES_NOT_EXIST"}, status=404)
        
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)
        
        except ValueError:
            return JsonResponse({"message": "VALUE_ERROR"}, status=400)


class PenaltyView(View):
    @login_decorator
    def put(self, request, penalty_id):
        try: 
            if request.user.role_id != Role.Type.ADMIN.value:
                return JsonResponse({"message": "UNAUTHORIZED"}, status = 401)
            
            data = json.loads(request.body)

            penalty_entity = DiscountOrPenalties.objects.get(id=penalty_id)

            if data["number"]:
                penalty_entity.number = data["number"]

            if data["description"]:
                penalty_entity.description = data["description"]

            penalty_entity.save()
            
            return JsonResponse({"result" : {"penalty" : penalty_entity.number,
                "description" : penalty_entity.description}}, status=200)

        except DiscountOrPenalties.DoesNotExist:
            return JsonResponse({"message": "PENALTY_DOES_NOT_EXIST"}, status=404)
        
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)
        
        except ValueError:
            return JsonResponse({"message": "VALUE_ERROR"}, status=400)
