"""Posts admin classes"""

#Django
from django.contrib import admin

#Models
from posts.models import Post

@admin.register(Post)                    ##Registro con decorador

class postAdmin(admin.ModelAdmin):
    """Admin posts"""

    list_display = ('pk', 'user', 'title', 'photo',)
    list_display_links = ('pk', 'user')                 ##Para entrar con el id, nombre
                                                        ##o telefono a la info del
                                                        ##usuario desde la vista admin

    ##Para editar los datos desde la vista de admin
    list_editable = ('title', 'photo')

    ##Para agregar barra de busqueda a la vista admin
    search_fields= (
        'user__username',            ##doble guion bajo '__' para hacer un query
        'title',                     ##especial
    )

    ##Informacion de los usuarios creados y modificados, las fechas y horas
    list_filter = (                 ##El orden en que se pongan, es el orden en el
        'user__is_active',          ##que sale la informacion
        'user__is_staff',
        'created',                  
        'modified'
    )

    readonly_fields = ('created', 'modified')   ##Cuando se acceda al detalle de un objeto que este
                                                ##dentro de esta variable, no se podra editar
