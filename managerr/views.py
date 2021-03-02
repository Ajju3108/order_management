from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import ModelViewSet
from .models import Project,Users
from .serializer import Project_seri

class project_view(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = Project_seri


from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def welcome(request):
    content = {"message": "Welcome to the order management project!"}
    return JsonResponse(content)


from .serializer import Order_seri
from .models import Order,Users
from rest_framework import status


@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def get_order(request):
    user = request.user.id
    orders = Order.objects.filter(added_by=user)
    serializer = Order_seri(orders, many=True)
    return JsonResponse({'orders': serializer.data}, safe=False, status=status.HTTP_200_OK)

from .models import Project
import json
from django.core.exceptions import ObjectDoesNotExist

@api_view(["POST"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def add_order(request):
    payload = json.loads(request.body)
    user = request.user
    try:
        project = Project.objects.get(id=payload["Project"])
        order = Order.objects.create(
            choices=payload["choices"],
            status=payload["status"],
            translated_text=payload["translated_text"],
            created_on=payload["created_on"],
            updated_on=payload["updated_on"],
            added_by=user,
            project=project
        )
        serializer = Order_seri(order)
        return JsonResponse({'order': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["PUT"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def update_order(request, id):
    user = request.user.id
    payload = json.loads(request.body)
    try:
        orders = Order.objects.filter(added_by=user, id=id)
        orders.update(**payload)
        order = Order.objects.get(id=id)
        serializer = Order_seri(order)
        return JsonResponse({'order': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["DELETE"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def delete_order(request, id):
    user = request.user.id
    try:
        order = Order.objects.get(added_by=user, id=id)
        order.delete()
        return JsonResponse(status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)