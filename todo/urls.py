from django.urls import path, include
from rest_framework.routers import DefaultRouter
from todo.views import TodoViewSet, UserViewSet, CurrentAuthenticatedUser

router = DefaultRouter()
router.register('todos', TodoViewSet, basename='todos')
router.register('users', UserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('current_user/', CurrentAuthenticatedUser.as_view(), name='current-user'),
]