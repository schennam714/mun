from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path("", views.index_view, name = "index"),
    path("leadership", views.leadership_view, name = "leadership"),
    path("calendar", views.calendar_view, name = "calendar"),
    path("mun101", views.mun101_view, name = "mun101"),
    path("index.html", views.index_view, name = "oldhome"),
    path("schedule.html", views.index_view, name = "oldsched"),
    path("committees.html", views.index_view, name = "oldcomms"),
    path("invitation.html", views.index_view, name = "oldinv"),
    path("techmun.html", views.index_view, name = "oldtech"),
    path("costsinfo.html", views.index_view, name = "oldcost"),
    path("secstaff.html", views.index_view, name = "oldsec"),

    

]

