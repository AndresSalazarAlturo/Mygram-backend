"""Mygram views"""
#Django
from django.http import HttpResponse
#Utilities
from datetime import date, datetime
import json


def hello_world(request):
    """Return a greeting"""
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs') ## En strftime se pasa el mes como %b,
    ## el dia como %dth, el año %Y, la hora %H y los minutos %M.                
    return HttpResponse('Hey there! Current server time is {now}'.format(now=now))

def sort_integers(request):
    """Return json responce with sorted integers"""
    # import pdb; pdb.set_trace()      ##Crea un debugger en la consola, hasta este punto, hasta que
                                        #Se escriba "c" + enter

    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)
     
    data = {
        'status': 'ok',
        'numbers': sorted_ints,
        'message': 'Integers sorted succesfully.'
    } 
    ##dumps convierte un diccionario a json, indent agrega indentacion al json
    return HttpResponse(
        json.dumps(data, indent = 4), 
        content_type= 'aplication/json'
    )

def say_hi(request, name, age):
    """"Return a greeting"""
    if age < 12:
        message = 'Sorry {}, you are not allowed here :('.format(name)
    else:
        message = 'Hi, {}! welcome to mygram'.format(name)
    
    return HttpResponse(message)
