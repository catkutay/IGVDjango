from django import forms
from .models import *


class recipieForm(forms.ModelForm):

    class Meta:
        model = Recipies
        fields = ['id', 'disease', 'description1', 'description2', 'description3', 'description4', 'image1', 'image2',
                  'image3', 'image4']