from .models import Booking, Menu
from django import forms
from django.forms import ModelForm

class BookingForm(forms.ModelForm):
    class Meta():
        model = Booking
        fields = '__all__'
        
class MenuForm(ModelForm):
    class Meta:
        model = Menu
        fields = '__all__'