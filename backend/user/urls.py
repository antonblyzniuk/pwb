from django.urls import path

from .views import UserRegistrationView, AdminRegistrationView


urlpatterns = [
    path("user/register/", UserRegistrationView.as_view(), name="register"),
    path("admin/register/", AdminRegistrationView.as_view(), name="admin-register"),
]
