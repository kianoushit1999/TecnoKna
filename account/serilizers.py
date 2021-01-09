from rest_framework import serializers
from .models import *


class UserSerilizers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'phone')