from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("extracted_text_list", views.extracted_text_list, name="extracted_text_list"),
    path("extracted_text_detail/<str:id>", views.extracted_text_detail, name="extracted_text_detail"),

    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
]