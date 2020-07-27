from django import forms



class user_form(forms.Form):
  user_form = forms.CharField()
  user_email = forms.EmailField()
  

