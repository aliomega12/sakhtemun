from django import forms
from appvahed.models import mdl_vahed,mdl_sakhtemoun

class frm_sakhtemoun(forms.ModelForm):
    class Meeta:
        model=mdl_sakhtemoun
        exclude=[]


class frm_vahed(forms.ModelForm):
    class Meta:
        model=mdl_vahed
        exclude=[]
        