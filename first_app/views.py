from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Musician, Album
from first_app import forms

# Create your views here.



def index (request):
  # SELECT * FROM Musician ORDER BY first_name
  musician_list= Musician.objects.order_by('first_name')
  diction={'text_1':'This is a list of Musician', 'musician': musician_list}
  return render (request, 'first_app/index.html', context=diction)


def form (request):
  new_form= forms.user_form()
  diction={ 'test_form': new_form, 'heading1': 'this form is created using Django library'}
  
  if request.method == 'POST':
    new_form=forms.user_form(request.POST)
    
    
    if new_form.is_valid():
      user_name = new_form.cleaned_data['user_name']
      user_email = new_form.cleaned_data['user_email']
      user_dob = new_form.cleaned_data['user_dob']
      boolean_field = new_form.cleaned_data['boolean_field']
      char_field = new_form.cleaned_data['char_field']
      choice_field=new_form.cleaned_data['choice_field']
      radio_field=new_form.cleaned_data['radio_field']
      
      
      
      diction.update({'user_name': user_name})
      diction.update({'user_email': user_email})
      diction.update({'user_dob': user_dob})
      diction.update({'boolean_field': boolean_field})
      diction.update({'char_field': char_field})
      diction.update({'choice_field': choice_field})
      diction.update({'radio_field': radio_field})
     
      diction.update({'field': new_form.cleaned_data['field']})
      
    
      diction.update({'form_submitted':'Yes'})
  
  
  return render(request, 'first_app/form.html', context=diction)
  




