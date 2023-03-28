from django import forms
from django.forms import ModelForm
from .models import Contact

# class PartnershipForm(ModelForm):

#     class Meta:
#         model = Partnership
#         fields = "__all__"

  
class ContactForm(ModelForm):

    class Meta:
        model = Contact
        fields = "__all__"
       
