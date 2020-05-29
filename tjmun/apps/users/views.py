from django.shortcuts import render, redirect
from django import http
from .models import User, Next_Conf
from .forms import PdfForm, DelForm
from django.forms import formset_factory
# Create your views here.

def upload(request):
    user = request.user
    instance = User.objects.get(pk = user.id)
    if user.is_authenticated:
        form = PdfForm(request.POST, request.FILES, instance = instance)
        if form.is_valid():
                form.save()
                #return redirect("users:index")
        return render(
            request,
            "members/forms.html",
            {
                "pdf_form": form,
            }
        )
    else:
        raise http.Http404

def warning(request):
    return render(request, "members/warning.html")

def home(request):
    user = request.user
    if user.is_authenticated:
        return render(request,"members/index.html")
    else:
        return redirect("auth:login")
def curr_dels(request):
    user = request.user
    instance = Next_Conf.objects.get(id=1)
    if user.is_officer:
        form = DelForm(request.POST, instance = instance)
        if form.is_valid():
                form.save()
                #return redirect("users:index")
        return render(
            request,
            "members/conflist.html",
            {
                "del_form": form,
            }
        )
    else:
        raise http.Http404   
        
def check_form(request):
    user = request.user
    #temps = User.objects.exclude(emergency_care_card__isnull=False, emergency_care_card__contains='ecc_forms', health_information__isnull=False, health_information__contains='health_forms')
    temps = Next_Conf.objects.get(id = 1).dels
    members = temps.order_by('full_name')
    fields = User._meta.fields
    if user.is_officer:
        return render(
            request,
            "members/list.html",
            {
                "members": members,
                "fields": fields,
            }
        )
    else:
        raise http.Http404