from django.urls import path
from .views import RegisterUserView,UserView,UserLoginView

urlpatterns = [
    path('register/',RegisterUserView.as_view(),name="register_view"),
    path('details/<int:pk>/',UserView.as_view(),name="user_view"),
    path('login/',UserLoginView.as_view(),name="login_view")
]
