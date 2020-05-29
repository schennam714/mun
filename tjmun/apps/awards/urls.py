from django.urls import path

from . import views

app_name = "awards"

urlpatterns = [
    path("", views.show_years, name = "years"),
    path("conference/<str:conference_url>", views.show_conf, name = "show_conf"),
    path("<str:year_url>", views.show_year, name = "show_year"),
]