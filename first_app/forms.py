from django import forms
from django.core import validators
from first_app import models



class  MusicianForm (forms.ModelForm):
  
  class Meta:
    model = models.Musician
    fields = "__all__"
    
    # jodi specific kono kicho bad dite chai, tahole  exclude use korbo.....    exclude =['first_name]
    
    # r jodi specific koyeta form rakhte chai, tahole fields use korbo....    fields= (' first_name', 'last_name')



