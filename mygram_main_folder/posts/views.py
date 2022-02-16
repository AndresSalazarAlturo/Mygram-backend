"""Posts views"""
#Django
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Forms
from posts.forms import PostForm

#Utilities
from datetime import datetime

# Models
from posts.models import Post

#posts = [
#    {
#        'title': 'Mont Blanc',
#        'user': {
#            'name': 'Yésica Cortés',
#            'picture': 'https://picsum.photos/60/60/?image=1027'
#        },
#        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
#        'photo': 'https://picsum.photos/800/600?image=1036',
#    },
#    {
#        'title': 'Via Láctea',
#        'user': {
#            'name': 'Christian Van der Henst',
#            'picture': 'https://picsum.photos/60/60/?image=1005'
#        },
#        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
#        'photo': 'https://picsum.photos/800/800/?image=903',
#    },
#    {
#        'title': 'Nuevo auditorio',
#        'user': {
#            'name': 'Uriel (thespianartist)',
#            'picture': 'https://picsum.photos/60/60/?image=883'
#        },
#        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
#        'photo': 'https://picsum.photos/500/700/?image=1076',
#    }
#]

# def list_posts(request):
#     """List existing posts"""
#     content = []
#     for post in posts:
#         content.append("""
#             <p><strong>{name}</strong></p>
#             <p><small>{user} - <i>{timestamp}</i></small></p>
#             <figure><img src = "{picture}"/></figure>
#             """.format(**post)          ##Con **post no es necesario poner name=name, user=user,
#         )                               ##picture=picture, sino que asi se obtienen todos.

#     return HttpResponse('<br>'.join(content))
@login_required             ##Login required como decorador de python
def list_posts(request):
    """List existing posts"""
    posts = Post.objects.all().order_by('-created')
    
    return render(request, 'posts/feed.html', {'posts': posts}) ##Busca dentro de los directorios de las
                                        ##aplicaciones que creamos en el folder 
                                        ##templates segun se ve en settings TEMPLATES

@login_required                         ##Tener sesion inciada obligatorimente
def create_post(request):
    """Create new post view."""
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('feed')

    else:
        form = PostForm()

    return render(
        request=request,
        template_name='posts/new.html',
        context={
            'form': form,
            'user': request.user,
            'profile': request.user.profile
        }
    )