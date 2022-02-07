"""Users views"""
#Django
import profile
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

#Models
from django.contrib.auth.models import User
from users.models import Profile

#Exceptions
from django.db.utils import IntegrityError

#Forms
from users.forms import ProfileForm

# Create your views here.

def update_profile(request):
    """Update users profile"""

    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data

            profile.website = data['website']
            profile.phone_number = data['phone_number']
            profile.biography = data['biography']
            profile.picture = data['picture']
            profile.save()
            
            return redirect('update_profile')
    else:
        form = ProfileForm()
        

    return render(request = request, 
    template_name='users/update_profile.html',
    context={
        'profile': profile,
        'user': request.user,
        'form': form,
    })
    

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

def signup_view(request):
    """Signup a user"""
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']

        if password != password_confirmation:
            return render('users/signup.html', {'error': 'Password confirmation does not match'})

        #Elevamos un error en caso de que se intente registrar con un username ya utilizado
        try:
            ##Si coinciden las contraseñas, entonces vamos a crear el usuario
            user = User.objects.create_user(username = username, password = password)
        except IntegrityError:
            #Damos un mensaje de error al ya existir ese usuario y ser lo mas especificos posibles en
            #el error que vamos a tomar, ya que pueden pasar muchos timpos de error o situaciones
            return render(request, 'users/signup.html', {'error': 'Username already used'})

        # EMAIL VALIDATION
        user.email = request.POST['email']
        if User.objects.filter(email=user.email):
            return render(request, 'users/signup.html', {'error': 'Email is already in used!'})

        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        
        user.save()

        #Crear una instancia de profile
        profile = Profile(user = user)
        #Siempre salvar los objetos
        profile.save()

        return redirect('login')

    return render(request, 'users/signup.html')

@login_required                          ##Con el decorador, evitamos que haga el logout de una sesion inexistente
def logout_view(request):
    """logout a user"""
    logout(request)
    return redirect('login')



