"""Users views"""
#Django
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login

# Create your views here.

def login_view(request):
    """Login view"""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username = username, password = password)
        if user:
            login(request, user)        ##Si hay un user, hago un login de request y user y se
                                        ##genera la sesion. Revisar documentacion 
            return redirect('feed')     ##Redirije al usuario a otra direccion para evitar que haga el 
                                        ##formulario mas de una vez
        else:
            return render(request, 'users/login.html', {'error' : 'Incorrect username and password'})


    return render(request, 'users/login.html')
