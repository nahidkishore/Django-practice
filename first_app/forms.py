from django import forms



class user_form(forms.Form):
  user_name = forms.CharField( label="Full Name", initial="nahid")
  
  user_email = forms.EmailField(label= "User Email",  widget =forms.TextInput(attrs= {'placeholder': 'Enter Your Email', 'style': 'width:300px'}))
  
  user_dob=forms.DateField(label= "Date of Birth", widget=forms.TextInput(attrs={'type': 'date'}))
  
  #user_dob1=forms.DateField(label= "Date of Birth", widget=forms.DateInput(attrs={'type': 'date'}))
  
  
  
  

