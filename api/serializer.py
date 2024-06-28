from rest_framework.serializers import ModelSerializer
from .models import product,cart_product
from django.contrib.auth.models import User
class productserializer(ModelSerializer):
    class Meta:
     model=product
     fields='__all__'


class cartserializer(ModelSerializer):
    class Meta:
      model=cart_product
      fields='__all__'


# User Serializer
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user