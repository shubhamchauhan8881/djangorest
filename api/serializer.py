from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length= 100)
    email = serializers.EmailField(max_length=100)
    username = serializers.CharField(max_length=50)
    is_staff = serializers.BooleanField()
    # 

class UserCreateSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=100)
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length= 100)


    def create(self, validated_data):
      
        new_user = User.objects.create(
            username= validated_data["username"],
            first_name= validated_data["first_name"],
            last_name= validated_data["last_name"]
        )

        new_user.set_password(validated_data["password"])
        new_user.save()

        return new_user