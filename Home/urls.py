from django.urls import path
from . import views
urlpatterns = [
    path("", views.home, name="home"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("greeting_card/<str:userID>/<str:greetID>/", views.greeting_card, name="greeting_card"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
]
