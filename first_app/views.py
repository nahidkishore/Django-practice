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
    diction.update({'test_form': new_form})
    
    
    
    if new_form.is_valid():
      diction.update({'field':'Fields Match !!'})
      
      diction.update({'form_submitted':'Yes'})
  
  
  return render(request, 'first_app/form.html', context=diction)
  




