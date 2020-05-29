import random

from django import http
from django.shortcuts import render, redirect, reverse, get_object_or_404

from .models import Conference, Year, Committee, Delegation
# Create your views here.

def show_conf(request, conference_url):
    conference = get_object_or_404(Conference, url = conference_url)

    return render(
        request,
        "awards/show.html",
        {
            "conference": conference,
            "committees": conference.committees.all
        },
    )


def show_years(request):
    temp = Year.objects.all()
    years = temp.order_by('-name')
    return render(
        request,
        "awards/index.html",
        {
            "years": years,
        },
    )

def show_year(request, year_url):
    year = get_object_or_404(Year, url = year_url)
    return render(
        request,
        "awards/year.html",
        {
            "year": year,
            "conferences": year.conferences.all,
        }
    )