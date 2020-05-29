from django.urls import path

from . import views

app_name = "users"

urlpatterns = [
    path("upload", views.upload, name = "upload"),
    path("", views.home, name = "index"),
    path("list", views.check_form, name = "list"),
    path("delegates", views.curr_dels, name = "dels"),
    path("warning", views.warning, name = "warning")
]

