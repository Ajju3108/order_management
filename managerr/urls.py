from django.urls import include, path
from .views import get_order,add_order,update_order,delete_order, project_view

# from rest_framework.routers import SimpleRouter
#
# router = SimpleRouter()
#
# router.register('projectapi',project_view)
#
# urlpatterns = router.urls


urlpatterns = [
  path('getorder', get_order),
  path('addorder', add_order),
  path('updatebook/<int:id>',update_order),
  path('deletebook/<int:id>', delete_order)
]


