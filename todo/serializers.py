from django.contrib.auth.models import User
from rest_framework import serializers
from todo.models import Todo

class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    This serializer helps to convert the django default
    User model python native objects into a json/xml
    according to the fields specified.
    """
    class Meta:
        model = User
        fields = ['url', 'username', 'password', 'first_name', 'last_name', 'email']

        extra_kwargs = {'password':{
            'write_only': True,
            'required': True

        }}

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
        )

        user.set_password(validated_data['password'])
        user.save()
        return user


class TodoSerializer(serializers.ModelSerializer):
    """
    This serializer helps to convert the python To do
    native objects into a json/xml according to the
    fields specified.
    """

    class Meta:
        model = Todo
        fields = ['id', 'tittle', 'body', 'date', 'done']








