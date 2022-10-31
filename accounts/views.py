from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm

def login (request):
    
    if request.method == 'POST':
                formulario= AuthenticationForm()
        
    else:
        formulario= AuthenticationForm()
        
    return render (request, 'accounts/login.html',{'formulario':formulario})
