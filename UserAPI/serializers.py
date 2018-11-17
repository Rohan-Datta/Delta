from rest_framework import serializers
from UserAPI.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('displayName','email','uid','company_name','company_type')
