"""Users views"""
#Django
from dataclasses import field
from pipes import Template
import profile
from re import template
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.generic import DetailView, FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView
from django.views.generic import ListView

#Models
from django.contrib.auth.models import User
from posts.models import Post
from users.models import Profile

#Forms
from users.forms import SignupForm
from users.models import Profile

class UserDetailView(LoginRequiredMixin, DetailView):
    """User detail view."""

    template_name = 'users/detail.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        """Add user's posts to context."""
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Post.objects.filter(user=user).order_by('-created')
        return context

#Se utiliza esta clase para no hacer el signup que es repetitivo al igual que se hizo con los views de posts
class SignUpView(FormView):
    """Users signup view"""
    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        """Save form data"""
        form.save()
        return super().form_valid(form)

class UpdateProfileView(LoginRequiredMixin, UpdateView):
    """Update profile view"""

    template_name = 'users/update_profile.html'
    model = Profile
    fields = ['website', 'biography', 'phone_number', 'picture']

    def get_object(self):
        """Return user's profile"""
        return self.request.user.profile

    def get_success_url(self):
        """Return to user's profile"""
        username = self.object.user.username
        return reverse('users:detail', kwargs = {'username' : username})

#@login_required                            #Como decorador para pedir un inicio de sesion obligario
#def update_profile(request):
#    """Update users profile"""
#
#    profile = request.user.profile
#    if request.method == 'POST':
#        form = ProfileForm(request.POST, request.FILES)
#        if form.is_valid():
#            data = form.cleaned_data
#
#            profile.website = data['website']
#            profile.phone_number = data['phone_number']
#            profile.biography = data['biography']
#            profile.picture = data['picture']
#            profile.save()
#            
#            return redirect('user:update')
#            url = reverse('users:detail', kwargs={'username': request.user.username})
#            return redirect(url)
#    else:
#        form = ProfileForm()
#        
#
#    return render(request = request, 
#    template_name='users/update_profile.html',
#    context={
#        'profile': profile,
#        'user': request.user,
#        'form': form,
#    })
#    

def login_view(request):
    """Login view"""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username = username, password = password)
        if user:
            login(request, user)                ##Si hay un user, hago un login de request y user y se
                                                ##genera la sesion. Revisar documentacion 
            return redirect('posts:feed')       ##Redirije al usuario a otra direccion para evitar que haga el 
                                                ##formulario mas de una vez
        else:
            return render(request, 'users/login.html', {'error' : 'Incorrect username and password'})


    return render(request, 'users/login.html')

#def signup_view(request):
#    """Signup View"""
#
#    if request.method == 'POST':
#        form = SignupForm(request.POST)
#        if form.is_valid():
#            form.save()
#            return redirect('users:login')
#    else: 
#        form = SignupForm()
#    return render(
#        request=request,
#        template_name='users/signup.html',
#        context={'form' : form}
#    )

    #if request.method == 'POST':
#
    #    username = request.POST['username']
    #    password = request.POST['password']
    #    password_confirmation = request.POST['password_confirmation']
#
    #    if password != password_confirmation:
    #        return render('users/signup.html', {'error': 'Password confirmation does not match'})
#
    #    #Elevamos un error en caso de que se intente registrar con un username ya utilizado
    #    try:
    #        ##Si coinciden las contraseñas, entonces vamos a crear el usuario
    #        user = User.objects.create_user(username = username, password = password)
    #    except IntegrityError:
    #        #Damos un mensaje de error al ya existir ese usuario y ser lo mas especificos posibles en
    #        #el error que vamos a tomar, ya que pueden pasar muchos timpos de error o situaciones
    #        return render(request, 'users/signup.html', {'error': 'Username already used'})
#
    #    # EMAIL VALIDATION
    #    user.email = request.POST['email']
    #    if User.objects.filter(email=user.email):
    #        return render(request, 'users/signup.html', {'error': 'Email is already in used!'})
#
    #    user.first_name = request.POST['first_name']
    #    user.last_name = request.POST['last_name']
    #    
    #    user.save()
#
    #    #Crear una instancia de profile
    #    profile = Profile(user = user)
    #    #Siempre salvar los objetos
    #    profile.save()
#
    #    return redirect('login')
#
    #return render(request, 'users/signup.html')

@login_required                          ##Con el decorador, evitamos que haga el logout de una sesion inexistente
def logout_view(request):
    """logout a user"""
    logout(request)
    return redirect('users:login')



