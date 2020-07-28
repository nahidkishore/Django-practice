from django import forms



class user_form(forms.Form):
  user_name = forms.CharField( label="Full Name", initial="nahid")
  
  user_email = forms.EmailField(label= "User Email",  widget =forms.TextInput(attrs= {'placeholder': 'Enter Your Email', 'style': 'width:300px'}))
  
  user_dob=forms.DateField(label= "Date of Birth", widget=forms.TextInput(attrs={'type': 'date'}))
  
  #user_dob1=forms.DateField(label= "Date of Birth", widget=forms.DateInput(attrs={'type': 'date'}))
  
  boolean_field= forms.BooleanField()
  char_field = forms.CharField(max_length=15, min_length=5)
  
  district=(
    ('', '-- select--'),
    
    (1, 'kishoregong'),
    (2, 'Dhaka'),
    (3, 'Gazipur'),
    (4, 'Rajshahi'),
    (5, 'feni'),
    (6, 'Narshingdhi'),
  )
  
  choice_field = forms.ChoiceField(choices= district )
  
  
  division=(('Dhaka', 'Dhaka'), ('Mymenshing', 'Mymenshing'), ('Chittagong', 'Chittagong'))
  
  Radio_field=forms.ChoiceField(choices=division, widget=forms.RadioSelect)
  
  
  
  choices = (('A','A'),('B','B'),('C','C'))
  field = forms.MultipleChoiceField(choices=choices, widget=forms.CheckboxSelectMultiple)
  
  
  
  

