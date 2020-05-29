from django import forms
from django.forms import formset_factory

from .models import User, Next_Conf

class PdfForm(forms.ModelForm):
    emergency_care_card = forms.FileField(required = False)#, null = True)
    health_information = forms.FileField(required = False)#, null = True)
    #luggage_search = forms.FileField(required = False)#, null = True)
    #parent_authorization = forms.FileField(required = False)#, null = True)
    #code_of_conduct = forms.FileField(required = False)#, null = True)
    #delegate_release = forms.FileField(required = False)#, null = True)


    class Meta:
        model = User
        fields = ["emergency_care_card", "health_information"]#, "parent_authorization", "code_of_conduct"]#, "luggage_search", "delegate_release"]

class DelForm(forms.ModelForm):
    dels = forms.ModelMultipleChoiceField(queryset = User.objects.all(), widget = forms.CheckboxSelectMultiple, required = False)
    
    class Meta:
        model = Next_Conf
        fields = ["dels"]