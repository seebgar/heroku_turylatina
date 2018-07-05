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
    




from django.core.mail import send_mail
from django.conf import settings

# COMO HACERLO? : https://www.codingforentrepreneurs.com/blog/use-gmail-for-email-in-django/

#from django.template.loader import render_to_string

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
                "info": "Bogotá is Colombia's beating heart, an engaging and vibrant capital cradled by chilly Andean peaks and steeped in sophisticated urban cool. The city's cultural epicenter is La Candelaria, the cobbled historic downtown to which most travelers gravitate. Here, a potpourri of preciously preserved colonial buildings house museums, restaurants, hotels and bars peppered amid 300-year-old homes, churches and convents. Nearly all of Bogotá's traditional attractions are here – radiating out from Plaza de Bolívar – and gorgeous Cerro de Monserrate is just east. \nContinue reading on https://www.lonelyplanet.com/colombia/bogota"
            },
            {
                "name": "Cartagena de Indias",
                "id": 2,
                "image": "https://upload.wikimedia.org/wikipedia/commons/c/cf/Street_in_Cartagena%2C_Colombia.jpg",
                "price": 299999,
                "dpt": "La Ciudad Amurallada",
                "info" : "Cartagena de Indias is the undisputed queen of the Caribbean coast, a fairy-tale city of romance, legends and superbly preserved beauty lying within an impressive 13km of centuries-old colonial stone walls. Cartagena's Old Town is a Unesco World Heritage site – a maze of cobbled alleys, balconies covered in bougainvillea, and massive churches that cast their shadows across leafy plazas. \nContinue reading on https://www.lonelyplanet.com/colombia/caribbean-coast/cartagena"
            },
            {
                "name": "Cali",
                "id": 3,
                "image": "https://upload.wikimedia.org/wikipedia/commons/c/ce/Calle_de_La_Escopeta%2C_Cali%2C_Colombia_01.jpg",
                "price": 149999,
                "dpt": "La Capital Mundial de la Salsa",
                "info" : "While it may not have the looks to front the tourist brochure, Cali is the kind of place that provides all the substance. It's a hot, gritty city with a passion for life that draws you in and stays with you long after you leave town. \nContinue reading on https://www.lonelyplanet.com/colombia/southwest-colombia/cali "
            },
            {
                "name": "Medellín",
                "id": 4,
                "image": "https://www.themasculinetraveler.com/wp-content/uploads/2017/02/Medellin-Columbia.jpg",
                "price": 189999,
                "dpt": "La Ciudad de la Eterna Primavera",
                "info" : "Medellín packs the punch of a city twice its size. Situated in a narrow valley, its skyline reaches for the heavens, setting high-rise apartment and office buildings against a backdrop of jagged peaks in every direction. Its pleasant climate gives it its nickname – the City of Eternal Spring – and the moderate temperatures put a spring in the locals' steps, at work and at play. It's a bustling place of industry and commerce, especially textile manufacturing and exported cut flowers. On weekends Medellín lets its hair down, its many discos attracting the beautiful people. \nContinue reading on https://www.lonelyplanet.com/colombia/northwest-colombia/medellin"
            },
            {
                "name": "Santa Marta",
                "id": 5,
                "image": "https://upload.wikimedia.org/wikipedia/commons/3/38/El_Rodadero%2C_Santa_Marta%2C_Colombia.jpg",
                "price": 299999,
                "dpt": "La Perla de América",
                "info" : "Santa Marta is South America's oldest European-founded town and the second most important colonial city on Colombia's Caribbean coast. Despite its long history and charming center, it gets a bad rap from many travelers, who rightly cite its unsightly urban sprawl and terrible traffic as reasons not to hang about here. The secret to Santa Marta is to use it for what it does well: hotels, restaurants and bars, and then get out to the slew of superb destinations nearby during the daytime. \nContinue reading on https://www.lonelyplanet.com/colombia/caribbean-coast/santa-marta"
            },
            {
                "name": "Barranquilla",
                "id": 6,
                "image": "https://cdn.colombia.com/images/turismo/sitios-turisticos/barranquilla/barranquilla.jpg",
                "price": 139999,
                "dpt": "La Puerta de Oro",
                "info" : "Barranquilla, Colombia's fourth-largest city, is a hardworking port town located on the delta of the massive River Magdalena and laid out in a tangled ribbon along mangroves and the Caribbean Sea, sweltering and hustling in the blinding sun. The birthplace of Colombian pop goddess Shakira, Barranquilla is actually most famous for its annual carnaval, when the town clocks off, puts on its glad rags and goes wild as it throws the country's biggest street party. \nContinue reading on https://www.lonelyplanet.com/colombia/barranquilla"
            },
            {
                "name": "Guaduas",
                "id": 8,
                "image": "http://magicalcolombia.com/wp-content/uploads/2017/06/main_square_guaduas_cundinamarca_travel_colombia-1.jpg",
                "price": 19999,
                "dpt": "Villa de San Miguel de Guaduas",
                "info" : "Guaduas is a town in Colombia, in the Lower Magdalena Province department of Cundinamarca, about 117 km from Bogotá. It is an agricultural and tourist center of some importance with a population of about 33,000. Its name refers to a type of bamboo cane. It is one of the cities on the Bogotá-Medellín highway. Its main plaza is featured on the Colombian ten-thousand pesos bill, and is one of the seats of the Roman Catholic Diocese of La Dorada–Guaduas"
            }
        ]
    }

    if request.method == 'POST':
        form = request.POST
        subject = "[TURYLATINA] Nuevo Cliente"
        message = f"Nombre: {form.get('name')} {form.get('lastname')} \nEmail: {form.get('email')} \nTelefono: {form.get('phone')} \nDestino: {form.get('destination')} \nFechas: desde {form.get('from_date')} hasta {form.get('to_date')}. \nMensaje: {form.get('extra')}"
        from_email = form.get('email')
        to_email = ["sebgarcia.26@gmail.com"]
        
        
        send_mail(subject=subject, message=message, from_email=from_email, recipient_list=to_email, fail_silently=True)
        return render(request, 'error.html', { 'message': "your message has been delivered succesfully", 'status': 'Thank you!' })

        


    return render(request, 'cities.html', context)



def map(request):
    return render(request, 'map.html')



def submit(request):
    return render(request, 'error.html', { 'message': "your message has been delivered succesfully", 'status': 'Thank you!' })


    




    