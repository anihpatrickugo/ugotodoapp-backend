from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.views import Token
from todo.models import Todo
from todo.serializers import TodoSerializer, UserSerializer

# Create your views here.


class TodoViewSet(viewsets.ModelViewSet):
    """
    This Viewset contains all the basic http methods
    for CRUD operations.
    """

    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]


    def get_queryset(self):
        queryset = self.queryset.filter(user=self.request.user)
        return queryset

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)





class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset contains the login and signup
    functionality of the user
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CurrentAuthenticatedUser(APIView):


    def get(self, request):
        token_key = self.request.headers.get('Authorization')
        user_id = Token.objects.get(key=token_key).user_id
        user = User.objects.get(id=user_id)
        return JsonResponse({
            "id": user.id,
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email
        })

