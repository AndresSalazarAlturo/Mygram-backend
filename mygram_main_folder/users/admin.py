"""User admin classes."""

# Django
from django.contrib import admin

# Models
from users.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile admin."""

    list_display = ('pk', 'user', 'phone_number', 'website', 'picture')
    list_display_links = ('pk', 'user') ##Para entrar con el id, nombre
                                                        ##o telefono a la info del
                                                        ##usuario desde la vista admin

    ##Para editar los datos desde la vista de admin
    list_editable = ('phone_number', 'website', 'picture')

    ##Para agregar barra de busqueda a la vista admin
    search_fields= (
        'user__username',           ##doble guion bajo '__' para hacer un query
        'user__email',              ##especial
        'user__first_name', 
        'user__last_name', 
        'phone_number'
    )

    ##Informacion de los usuarios creados y modificados, las fechas y horas
    list_filter = (                 ##El orden en que se pongan, es el orden en el
        'user__is_active',          ##que sale la informacion
        'user__is_staff',
        'created',                  
        'modified'
    )


    

