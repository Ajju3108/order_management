

from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url

from rest_framework.routers import SimpleRouter
from managerr import views

router = SimpleRouter()

router.register('projectapi',views.project_view,basename='project')

from rest_framework.schemas import get_schema_view      # swagger documetations
from rest_framework.renderers import CoreJSONRenderer
schema_view = get_schema_view(title='Swagger docs emp',renderer_classes=[CoreJSONRenderer])

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'swaggerdoc/', schema_view, name='docs'),
    url(r'^api-auth/', include('rest_framework.urls')),
    path('', include('managerr.urls')),
    url('', include(router.urls)),

]


