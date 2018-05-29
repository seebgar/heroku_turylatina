import os

from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse

# from the current directory > models
from .models import Greeting, City

import requests
import json



global converter_1
global converter_2


def exhange( wanted, amount ):
    '''
    API FREE CURRENCY CONVERTER real time currency rates
    '''
    converter_1 =  -1
    converter_2 = -1

    #currencies = 'USD,CAD,COP,MXN,ARS,BRL,CLP,EUR'
    
    if converter_1 == -1 or converter_2 == -1 :
        r = requests.get('http://free.currencyconverterapi.com/api/v5/convert',
                        params={ "q" : 'EUR_COP',"compact" : 'y' })
        converter_1 = r
        
        r_f = requests.get('http://free.currencyconverterapi.com/api/v5/convert',
                        params={ "q" : f'EUR_{wanted}',"compact" : 'y' })
        converter_2 = r_f

    if converter_1.status_code != 200 or converter_2.status_code != 200:
        return r.status_code
    
    data = converter_1.json()
    data_f = converter_2.json()

    euro = amount / data['EUR_COP']['val']
    total = euro * data_f[f'EUR_{wanted}']['val']

    return total
    








# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    #dataset City.objects.all()
    context = {
        'cities': [
            {
                "name": "Bogotá DC",
                "id": 1,
                "image": "https://c1.staticflickr.com/5/4335/36415484834_b2ae1f40f3_b.jpg",
                "price": 215999,
                "dpt": "La Atenas Suramericana",
                 "currencies": [ 
                    ("USD" , exhange(wanted='USD', amount=215999 ) ) ,
                    ("EUR" , exhange(wanted='EUR', amount=215999 ) ),
                    ("MXN" , exhange(wanted='MXN', amount=215999 ) ),
                    ("ARS" , exhange(wanted='ARS', amount=215999 ) ),
                    ("BRL" , exhange(wanted='BRL', amount=215999 ) ),
                    ("CLP" , exhange(wanted='CLP', amount=215999 ) )
                ]
            },
            {
                "name": "Cartagena de Indias",
                "id": 2,
                "image": "https://upload.wikimedia.org/wikipedia/commons/c/cf/Street_in_Cartagena%2C_Colombia.jpg",
                "price": 299999,
                "dpt": "La Ciudad Amurallada",
                 "currencies": [ 
                    ("USD" , exhange(wanted='USD', amount=299999 ) ) ,
                    ("EUR" , exhange(wanted='EUR', amount=299999 ) ),
                    ("MXN" , exhange(wanted='MXN', amount=299999 ) ),
                    ("ARS" , exhange(wanted='ARS', amount=299999 ) ),
                    ("BRL" , exhange(wanted='BRL', amount=299999 ) ),
                    ("CLP" , exhange(wanted='CLP', amount=299999 ) )
                ]
            },
            {
                "name": "Cali",
                "id": 3,
                "image": "https://upload.wikimedia.org/wikipedia/commons/c/ce/Calle_de_La_Escopeta%2C_Cali%2C_Colombia_01.jpg",
                "price": 149999,
                "dpt": "La Capital Mundial de la Salsa",
                 "currencies": [ 
                    ("USD" , exhange(wanted='USD', amount=149999 ) ) ,
                    ("EUR" , exhange(wanted='EUR', amount=149999 ) ),
                    ("MXN" , exhange(wanted='MXN', amount=149999 ) ),
                    ("ARS" , exhange(wanted='ARS', amount=149999 ) ),
                    ("BRL" , exhange(wanted='BRL', amount=149999 ) ),
                    ("CLP" , exhange(wanted='CLP', amount=149999 ) )
                ]
            },
            {
                "name": "Medellín",
                "id": 4,
                "image": "https://www.themasculinetraveler.com/wp-content/uploads/2017/02/Medellin-Columbia.jpg",
                "price": 189999,
                "dpt": "La Ciudad de la Eterna Primavera",
                 "currencies": [ 
                    ("USD" , exhange(wanted='USD', amount=189999 ) ) ,
                    ("EUR" , exhange(wanted='EUR', amount=189999 ) ),
                    ("MXN" , exhange(wanted='MXN', amount=189999 ) ),
                    ("ARS" , exhange(wanted='ARS', amount=189999 ) ),
                    ("BRL" , exhange(wanted='BRL', amount=189999 ) ),
                    ("CLP" , exhange(wanted='CLP', amount=189999 ) )
                ]
            },
            {
                "name": "Santa Marta",
                "id": 5,
                "image": "https://upload.wikimedia.org/wikipedia/commons/3/38/El_Rodadero%2C_Santa_Marta%2C_Colombia.jpg",
                "price": 299999,
                "dpt": "La Perla de América",
                 "currencies": [ 
                    ("USD" , exhange(wanted='USD', amount=299999 ) ) ,
                    ("EUR" , exhange(wanted='EUR', amount=299999 ) ),
                    ("MXN" , exhange(wanted='MXN', amount=299999 ) ),
                    ("ARS" , exhange(wanted='ARS', amount=299999 ) ),
                    ("BRL" , exhange(wanted='BRL', amount=299999 ) ),
                    ("CLP" , exhange(wanted='CLP', amount=299999 ) )
                ]
            },
            {
                "name": "Barranquilla",
                "id": 6,
                "image": "https://cdn.colombia.com/images/turismo/sitios-turisticos/barranquilla/barranquilla.jpg",
                "price": 139999,
                "dpt": "La Puerta de Oro",
                "currencies": [ 
                    ("USD" , exhange(wanted='USD', amount=139999 ) ) ,
                    ("EUR" , exhange(wanted='EUR', amount=139999 ) ),
                    ("MXN" , exhange(wanted='MXN', amount=139999 ) ),
                    ("ARS" , exhange(wanted='ARS', amount=139999 ) ),
                    ("BRL" , exhange(wanted='BRL', amount=139999 ) ),
                    ("CLP" , exhange(wanted='CLP', amount=139999 ) )
                ]
            },
            {
                "name": "Guaduas",
                "id": 8,
                "image": "http://magicalcolombia.com/wp-content/uploads/2017/06/main_square_guaduas_cundinamarca_travel_colombia-1.jpg",
                "price": 19999,
                "dpt": "Villa de San Miguel de Guaduas",
                 "currencies": [ 
                    ("USD" , exhange(wanted='USD', amount=19999 ) ) ,
                    ("EUR" , exhange(wanted='EUR', amount=19999 ) ),
                    ("MXN" , exhange(wanted='MXN', amount=19999 ) ),
                    ("ARS" , exhange(wanted='ARS', amount=19999 ) ),
                    ("BRL" , exhange(wanted='BRL', amount=19999 ) ),
                    ("CLP" , exhange(wanted='CLP', amount=19999 ) )
                ]
            }
        ]
    }

    return render(request, 'cities.html', context)



def map(request):
    return render(request, 'map.html')



def detail(request, id):
    return render(request, 'map.html')
    """ 
    context = {
        'cities': [
            {
                "name": "Bogotá DC",
                "id": 1,
                "image": "https://c1.staticflickr.com/5/4335/36415484834_b2ae1f40f3_b.jpg",
                "price": 215999,
                "dpt": "La Atenas Suramericana",
                 "currencies": [ 
                    ("USD" , exhange(wanted='USD', amount=215999 ) ) ,
                    ("EUR" , exhange(wanted='EUR', amount=215999 ) ),
                    ("MXN" , exhange(wanted='MXN', amount=215999 ) ),
                    ("ARS" , exhange(wanted='ARS', amount=215999 ) ),
                    ("BRL" , exhange(wanted='BRL', amount=215999 ) ),
                    ("CLP" , exhange(wanted='CLP', amount=215999 ) )
                ]
            },
            {
                "name": "Cartagena de Indias",
                "id": 2,
                "image": "https://upload.wikimedia.org/wikipedia/commons/c/cf/Street_in_Cartagena%2C_Colombia.jpg",
                "price": 299999,
                "dpt": "La Ciudad Amurallada",
                 "currencies": [ 
                    ("USD" , exhange(wanted='USD', amount=299999 ) ) ,
                    ("EUR" , exhange(wanted='EUR', amount=299999 ) ),
                    ("MXN" , exhange(wanted='MXN', amount=299999 ) ),
                    ("ARS" , exhange(wanted='ARS', amount=299999 ) ),
                    ("BRL" , exhange(wanted='BRL', amount=299999 ) ),
                    ("CLP" , exhange(wanted='CLP', amount=299999 ) )
                ]
            },
            {
                "name": "Cali",
                "id": 3,
                "image": "https://upload.wikimedia.org/wikipedia/commons/c/ce/Calle_de_La_Escopeta%2C_Cali%2C_Colombia_01.jpg",
                "price": 149999,
                "dpt": "La Capital Mundial de la Salsa",
                 "currencies": [ 
                    ("USD" , exhange(wanted='USD', amount=149999 ) ) ,
                    ("EUR" , exhange(wanted='EUR', amount=149999 ) ),
                    ("MXN" , exhange(wanted='MXN', amount=149999 ) ),
                    ("ARS" , exhange(wanted='ARS', amount=149999 ) ),
                    ("BRL" , exhange(wanted='BRL', amount=149999 ) ),
                    ("CLP" , exhange(wanted='CLP', amount=149999 ) )
                ]
            },
            {
                "name": "Medellín",
                "id": 4,
                "image": "https://www.themasculinetraveler.com/wp-content/uploads/2017/02/Medellin-Columbia.jpg",
                "price": 189999,
                "dpt": "La Ciudad de la Eterna Primavera",
                 "currencies": [ 
                    ("USD" , exhange(wanted='USD', amount=189999 ) ) ,
                    ("EUR" , exhange(wanted='EUR', amount=189999 ) ),
                    ("MXN" , exhange(wanted='MXN', amount=189999 ) ),
                    ("ARS" , exhange(wanted='ARS', amount=189999 ) ),
                    ("BRL" , exhange(wanted='BRL', amount=189999 ) ),
                    ("CLP" , exhange(wanted='CLP', amount=189999 ) )
                ]
            },
            {
                "name": "Santa Marta",
                "id": 5,
                "image": "https://upload.wikimedia.org/wikipedia/commons/3/38/El_Rodadero%2C_Santa_Marta%2C_Colombia.jpg",
                "price": 299999,
                "dpt": "La Perla de América",
                 "currencies": [ 
                    ("USD" , exhange(wanted='USD', amount=299999 ) ) ,
                    ("EUR" , exhange(wanted='EUR', amount=299999 ) ),
                    ("MXN" , exhange(wanted='MXN', amount=299999 ) ),
                    ("ARS" , exhange(wanted='ARS', amount=299999 ) ),
                    ("BRL" , exhange(wanted='BRL', amount=299999 ) ),
                    ("CLP" , exhange(wanted='CLP', amount=299999 ) )
                ]
            },
            {
                "name": "Barranquilla",
                "id": 6,
                "image": "https://cdn.colombia.com/images/turismo/sitios-turisticos/barranquilla/barranquilla.jpg",
                "price": 139999,
                "dpt": "La Puerta de Oro",
                "currencies": [ 
                    ("USD" , exhange(wanted='USD', amount=139999 ) ) ,
                    ("EUR" , exhange(wanted='EUR', amount=139999 ) ),
                    ("MXN" , exhange(wanted='MXN', amount=139999 ) ),
                    ("ARS" , exhange(wanted='ARS', amount=139999 ) ),
                    ("BRL" , exhange(wanted='BRL', amount=139999 ) ),
                    ("CLP" , exhange(wanted='CLP', amount=139999 ) )
                ]
            },
            {
                "name": "Guaduas",
                "id": 8,
                "image": "http://magicalcolombia.com/wp-content/uploads/2017/06/main_square_guaduas_cundinamarca_travel_colombia-1.jpg",
                "price": 19999,
                "dpt": "Villa de San Miguel de Guaduas",
                 "currencies": [ 
                    ("USD" , exhange(wanted='USD', amount=19999 ) ) ,
                    ("EUR" , exhange(wanted='EUR', amount=19999 ) ),
                    ("MXN" , exhange(wanted='MXN', amount=19999 ) ),
                    ("ARS" , exhange(wanted='ARS', amount=19999 ) ),
                    ("BRL" , exhange(wanted='BRL', amount=19999 ) ),
                    ("CLP" , exhange(wanted='CLP', amount=19999 ) )
                ]
            }
        ]
    }

    for x in range(0, (len(context) + 1)):
        if context['cities'][x]['id'] == id:
            context_detailed = {
                "city" : context['cities'][x]
            }
            return render(request, 'city.html', context_detailed)

    return render(request, 'error.html', { "message": "City does not exist ... o todavia no termino", "status": 404 })
 """
     
     

    




    