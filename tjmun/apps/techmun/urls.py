from django.urls import path

from . import views

app_name = "techmun"

urlpatterns = [
    path("committees", views.show_commtypes, name = "commtypes"),
    path("charity", views.charity_view, name = "charity"),
    path("costinfo", views.cost_view, name = "cost"),
    path("", views.index_view, name = "index"),
    path("invitation", views.invitation_view, name = "invitation"),
    path("positionpapers", views.position_view, name = "position"),
    path("registration", views.registration_view, name = "registration"),
    path("schedule", views.schedule_view, name = "schedule"),
    path("secstaff", views.secstaff_view, name = "secstaff"),
    path("<str:committee_url>", views.show_committee, name = "show_committee"),
]