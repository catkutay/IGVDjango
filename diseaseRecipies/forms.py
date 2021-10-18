from django import forms
from .models import *


class RecipeForm(forms.ModelForm):

    class Meta:
        model = Recipies
        fields = ['id','name', 'disease','image1', 'description1', 'image2', 'description2', 'image3', 'description3',
                  'image4', 'description4',
                  ]

        widget = {

            'disease': forms.Select(attrs={'class': 'form-control'}),
            'audio': forms.FileInput(attrs={'class': 'form-control'}),
            'image1': forms.FileInput(attrs={'class': 'form-control'}),
            'description1': forms.Textarea(attrs={'class': 'form-control'}),
            'image2': forms.FileInput(attrs={'class': 'form-control'}),
            'description2': forms.Textarea(attrs={'class': 'form-control'}),
            'image3': forms.FileInput(attrs={'class': 'form-control'}),
            'description3': forms.Textarea(attrs={'class': 'form-control'}),
            'image4': forms.FileInput(attrs={'class': 'form-control'}),
            'description4': forms.Textarea(attrs={'class': 'form-control'})

        }
