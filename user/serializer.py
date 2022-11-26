from rest_framework import serializers
from .models import UserModel
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.models import update_last_login
from rest_framework_simplejwt.tokens import RefreshToken

# Signup
User = get_user_model()

class UserSignupSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, max_length=50)
    username = serializers.CharField(required=True, max_length=30)
    password = serializers.CharField(required=True, write_only=True,style= {'input_type':'password'})
    profilePhoto = serializers.CharField(required=False, default="Nonedata", max_length=30)
    location = serializers.CharField(required=False,default="Nonedata", max_length=20)

    class Meta(object):
        model = UserModel
        fields = ['id','email','username', 'password', 'profilePhoto','location']

    def save(self, request):
        user = super().save()
        user.email = self.validated_data['email']
        user.set_password(self.validated_data['password'])
        user.save()
        return user

    def validate(self, data):
        email = data.get('email', None)
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({"msg": "이미 존재하는 이메일입니다.", "status":200})
        username = data.get('username', None)

        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({"msg": "이미 존재하는 사용자 이름입니다."})
        return data

class UserCheckSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = UserModel
        fields = ['email']
        
    def validate(self,data):
        email = data.get('email', None)
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({"msg":"이미 존재하는 이메일입니다.","status":200})
    