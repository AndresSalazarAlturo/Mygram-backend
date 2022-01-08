"""User admin classes."""

# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Models
from django.contrib.auth.models import User
from users.models import Profile


@admin.register(Profile)                    ##Registro con decorador
class ProfileAdmin(admin.ModelAdmin):
    """Profile admin."""

    list_display = ('pk', 'user', 'phone_number', 'website', 'picture')
    list_display_links = ('pk', 'user')                 ##Para entrar con el id, nombre
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

    fieldsets = (                               ##Organizar los datos segun se quieran visualizar
        ('Profile', {                           ##la vista de admin.
            'fields': (                         ##Esta hecho con tuplas y diccionarios
                ('user', 'picture'),),
        }),
        ('Extra info', {
            'fields':(
                ('website', 'phone_number'),
                ('biography')
            )
        }),
        ('Metadata',{
            'fields':(
                ('created', 'modified'),
            )
        })
    )

    readonly_fields = ('created', 'modified')   ##Cuando se acceda al detalle de un objeto que este
                                                ##dentro de esta variable, no se podra editar

class ProfileInLine(admin.StackedInline):       ##Para extender el modelo de usuario y agregar toda la info
    """Profile in line admin for users"""       ##desde una misma interfaz, por lo que al agregar un usuario
    model = Profile                             ##tenemos la opcion de agregar la informacion del perfil.
    can_delete = False
    verbose_name_plural = 'profiles'

class UserAdmin(BaseUserAdmin):                 ##Crea un nuevo admin de user, que hereda del base, por lo que se
    """Add profile admin to base user admin"""  ##importa UserAdmin como BaseUser Admin
    inlines = (ProfileInLine,)                  ##Se registran los in lines de esa clase en una tupla
    list_display = (                            ##Esta parte para entender que lo que hace es sonbrecribir la base
        'username',                             ##que ya existe y mostrarlo en desde la vista de usuarios en las
        'email',                                ##columnas.
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )

admin.site.unregister(User)                     ##Se sale del registro del ya existente y luego registra el usuario
admin.site.register(User, UserAdmin)            ##que creamos para poder agregar toda la informacion que se busca
                                                ##desde la misma intefaz. 
                                                ##El register puede recibir solo un modelo, tambien puede recibir un modelo
                                                ##y la clase admin que vamos a usar.


    

