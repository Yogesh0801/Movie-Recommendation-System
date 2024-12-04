# recommendations/forms.py
from django import forms

class RecommendationForm(forms.Form):
    movie_name = forms.CharField(label='Movie Name', max_length=100)
from recommendations.models import ClientRegister_Model


class ClientRegister_Form(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField(required=True)

    class Meta:
        model = ClientRegister_Model
        fields = ("username","email","password","phoneno","country","state","city")