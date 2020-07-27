from django import forms



class user_form(forms.Form):
  user_form = forms.CharField( label="Full Name", initial="nahid")
  user_email = forms.EmailField(label= "User Email")
  

