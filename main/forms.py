from django import forms
from .models import Lungcancerdetection


# Create your forms here.
class MovieForm(forms.ModelForm):

    class Meta:
        model = Lungcancerdetection;
        fields = ('file', 'image')