from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from accounts.views.auth_views import RegisterAPIView, LoginAPIView
from accounts.views.jwt_views import CustomTokenObtainPairView

urlpatterns = [
    path(
        "register/",
        RegisterAPIView.as_view(),
        name="register"
    ),
    path(
        "login/",
        LoginAPIView.as_view(),
        name="login"
    ),
    path(
        "login/jwt/",
        CustomTokenObtainPairView.as_view(),
        name="register"
    ),
    path("refresh/jwt/", TokenRefreshView.as_view(), name="refresh"),

]