from ItemsAPI.models import Laptop, Server, Accessory, GPU
from rest_framework import serializers


class LaptopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Laptop
        fields = ('__all__')

class ServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Server
        fields = ('__all__')

class AccessorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Accessory
        fields = ('__all__')

class GPUSerializer(serializers.ModelSerializer):
    class Meta:
        model = GPU
        fields = ('__all__')