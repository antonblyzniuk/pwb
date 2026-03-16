from django.urls import path

from .views import UserRegistrationView, AdminRegistrationView, MyInfoView


urlpatterns = [
    path("user/register/", UserRegistrationView.as_view(), name="register"),
    path("admin/register/", AdminRegistrationView.as_view(), name="admin-register"),
    path("user/my-info/", MyInfoView.as_view(), name="my-info"),
]
