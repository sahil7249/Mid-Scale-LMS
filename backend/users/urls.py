from django.urls import path
from .views import RegisterUserView,UserView

urlpatterns = [
    path('register/',RegisterUserView.as_view(),name="register_view"),
    path('details/<int:pk>/',UserView.as_view(),name="user_view")
]
