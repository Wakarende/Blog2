from django.urls import Path
from .views import RegisterView,LoginView,UserView,LogoutView

urlpatterns = [
  path('register/', RegisterView.as_view(), name="register"),
  path('login/', LoginView.as_view(), name="login"),
  path('user/', UserView.as_view()),
  path('logout/', LogoutView.as_view()),
]
