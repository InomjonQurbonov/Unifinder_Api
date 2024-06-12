from rest_framework import serializers
from app_users.models import User, PasswordResets, Author
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

UserModel = get_user_model()

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['country']

class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['phone_number', 'gender', 'affiliation']
        
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])
    info = InfoSerializer(required=True)
    author = AuthorSerializer(required=True)

    class Meta:
        model = UserModel
        fields = ('username', 'email', 'password', 'first_name', 'last_name', 'info', 'author')

    def create(self, validated_data):
        info_data = validated_data.pop('info')
        author_data = validated_data.pop('author')
        user = UserModel.objects.create_user(**validated_data)
        User.objects.create(user=user, **info_data)
        Author.objects.create(user=user, **author_data)
        return user
    
    def update(self, instance, validated_data):
        info_data = validated_data.pop('info', None)
        author_data = validated_data.pop('author', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if info_data:
            info = instance.info
            for attr, value in info_data.items():
                setattr(info, attr, value)
            info.save()
        
        if author_data:
            author = instance.author
            for attr, value in author_data.items():
                setattr(author, attr, value)
            author.save()

        return instance

class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        if not UserModel.objects.filter(email=value).exists():
            raise serializers.ValidationError("User with this email does not exist.")
        return value