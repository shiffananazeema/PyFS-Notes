from django import forms

# class Form(forms.Form):

#     title = forms.CharField(max_length=200)
#     description = forms.CharField(widget=forms.Textarea)
#     image = forms.ImageField()

from .models import Model

class Form(forms.ModelForm):
    class Meta:
        model = Model
        fields = ['title', 'description', 'image']