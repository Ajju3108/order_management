from .models import Users,Project,Order,Notification
from rest_framework.serializers import ModelSerializer

class user_seri(ModelSerializer):
    class Meta:
        model = Users
        fields ='__all__'

class Project_seri(ModelSerializer):
    class Meta:
        model = Project
        fields ='__all__'

class Order_seri(ModelSerializer):
    class Meta:
        model = Order
        fields ='__all__'

class Notification_seri(ModelSerializer):
    class Meta:
        model = Notification
        fields ='__all__'