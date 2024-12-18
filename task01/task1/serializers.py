from rest_framework.serializers import ModelSerializer
from .models import MyModel

class MyModelSerializer(ModelSerializer):
    class Meta:
        model = MyModel
        fields = ['id', 'name', 'description']