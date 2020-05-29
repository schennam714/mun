import random

from django import http
from django.shortcuts import render, redirect, reverse, get_object_or_404

from .models import Techmuncommittee, Commtype, Chair
# Create your views here.

def show_committee(request, committee_url):
    committee = get_object_or_404(Techmuncommittee, url = committee_url)

    return render(
        request,
        "techmun/committee/show.html",
        {
            "committee": committee
        },
    )

def show_commtypes(request):
    commtypes = Commtype.objects.all()
    return render(
        request,
        "techmun/committee/index.html",
        {
            "commtypes": commtypes,
        }
    )

def invitation_view(request):
    return render(request, "techmun/info/invitation.html")

def index_view(request):
    return render(request, "techmun/info/index.html")

def charity_view(request):
    return render(request, "techmun/info/charity.html")

def cost_view(request):
    return render(request, "techmun/info/costinfo.html")

def position_view(request):
    return render(request, "techmun/info/positionpapers.html")

def registration_view(request):
    return render(request, "techmun/info/registration.html")

def schedule_view(request):
    return render(request, "techmun/info/schedule.html")

def secstaff_view(request):
    return render(request, "techmun/info/secstaff.html")