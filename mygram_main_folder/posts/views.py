"""Posts views"""
#Django
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

#Utilities
from datetime import datetime
import json

posts = [
    {
        'title': 'Mont Blanc',
        'user': {
            'name': 'Yésica Cortés',
            'picture': 'https://picsum.photos/60/60/?image=1027'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/600?image=1036',
    },
    {
        'title': 'Via Láctea',
        'user': {
            'name': 'Christian Van der Henst',
            'picture': 'https://picsum.photos/60/60/?image=1005'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/800/?image=903',
    },
    {
        'title': 'Nuevo auditorio',
        'user': {
            'name': 'Uriel (thespianartist)',
            'picture': 'https://picsum.photos/60/60/?image=883'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/500/700/?image=1076',
    }
]

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

def list_posts(request):
    """List existing posts"""
    return render(request, 'feed.html', {'posts': posts}) ##Busca dentro de los directorios de las
                                        ##aplicaciones que creamos en el folder 
                                        ##templates segun se ve en settings TEMPLATES
