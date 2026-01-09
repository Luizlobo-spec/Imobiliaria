from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ViewsetUser, LoginView, LogoutView

router = DefaultRouter()
router.register('User', ViewsetUser, basename='User')

urlpatterns = [
    path('',include(router.urls)),
    path('login',LoginView.as_view(), name = 'login'),
    path("logout", LogoutView.as_view(), name="logout")]