"""Posts views."""

# Django
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, CreateView, ListView
from django.urls import reverse_lazy

# Forms
from posts.forms import PostForm

# Models
from posts.models import Post


class PostsFeedView(LoginRequiredMixin, ListView):
    """Return all published posts."""

    template_name = 'posts/feed.html'
    model = Post
    ordering = ('-created',)
    paginate_by = 30
    context_object_name = 'posts'

class PostsDetailView(LoginRequiredMixin, DetailView):
    """Return post detail"""

    template_name = 'posts/detail.html'
    queryset = Post.objects.all()
    context_object_name = 'post'

class CreatePostView(LoginRequiredMixin, CreateView):
    """Create a new post"""

    template_name = 'posts/new.html'
    form_class = PostForm
    success_url = reverse_lazy('posts:feed')

    def get_context_data(self, **kwargs):
        """Add user and profile to context"""
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profile
        return context


#@login_required             ##Login required como decorador de python
#def list_posts(request):
#    """List existing posts"""
#    posts = Post.objects.all().order_by('-created')
#    
#    return render(request, 'posts/feed.html', {'posts': posts}) ##Busca dentro de los directorios de las
#                                        ##aplicaciones que creamos en el folder 
#                                        ##templates segun se ve en settings TEMPLATES

#@login_required                         ##Tener sesion inciada obligatorimente
#def create_post(request):
#    """Create new post view."""
#    if request.method == 'POST':
#        form = PostForm(request.POST, request.FILES)
#        if form.is_valid():
#            form.save()
#            return redirect('posts:feed')
#
#    else:
#        form = PostForm()
#
#    return render(
#        request=request,
#        template_name='posts/new.html',
#        context={
#            'form': form,
#            'user': request.user,
#            'profile': request.user.profile
#        }
#    )