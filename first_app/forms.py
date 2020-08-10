from django import forms
from first_app import models

class MusicianForm(forms.ModelForm):
    class Meta:
        model = models.Musician
        fields = "__all__"
        
        
        
        
class AlbumForm(forms.ModelForm):
    release_date = forms.DateField(widget=forms.TextInput(attrs={'type':'date'}))
    class Meta:
        model = models.Album
        fields = "__all__"






    
    # jodi specific kono kicho bad dite chai, tahole  exclude use korbo.....    exclude =['first_name]
    
    # r jodi specific koyeta form rakhte chai, tahole fields use korbo....    fields= (' first_name', 'last_name')



