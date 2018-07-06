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
                "image": "Bogota.jpg",
                "vertical": "Bogota_2.jpg",
                "price": 215999,
                "dpt": "La Atenas Suramericana",
                "info": "Bogotá is Colombia's beating heart, an engaging and vibrant capital cradled by chilly Andean peaks and steeped in sophisticated urban cool. The city's cultural epicenter is La Candelaria, the cobbled historic downtown to which most travelers gravitate. Here, a potpourri of preciously preserved colonial buildings house museums, restaurants, hotels and bars peppered amid 300-year-old homes, churches and convents. Nearly all of Bogotá's traditional attractions are here – radiating out from Plaza de Bolívar – and gorgeous Cerro de Monserrate is just east. \nContinue reading on https://www.lonelyplanet.com/colombia/bogota",
                "ims": [
                    "https://i.pinimg.com/564x/37/0b/12/370b12a8721932d4d505e9132c045879.jpg",
                    "https://i.pinimg.com/564x/8b/42/3f/8b423f925341544ea50b3cc92173a4cc.jpg",
                    "https://i.pinimg.com/564x/6c/68/b3/6c68b355478d39dc2b81e2ac1befe12d.jpg",
                    "https://i.pinimg.com/564x/5c/35/91/5c359148b2c898e97ef6d15a265e20ef.jpg",
                    "https://i.pinimg.com/564x/30/a6/b1/30a6b16533a780017fa189a821011214.jpg",
                    "https://i.pinimg.com/564x/23/b2/4c/23b24cc48e3aeef0607c6ee16e5149d1.jpg",
                    "https://i.pinimg.com/564x/e4/17/0d/e4170d6a713faceb4e0436a0b9585c8e.jpg",
                    "https://i.pinimg.com/564x/dd/2f/4e/dd2f4e9c1e1d7da0924a9e8e390dc51d.jpg"

                ]
            },
            {
                "name": "Cartagena de Indias",
                "id": 2,
                "image": "Cartagena.jpg",
                "vertical": "Cartagena_2.jpg",
                "price": 299999,
                "dpt": "La Ciudad Amurallada",
                "info" : "Cartagena de Indias is the undisputed queen of the Caribbean coast, a fairy-tale city of romance, legends and superbly preserved beauty lying within an impressive 13km of centuries-old colonial stone walls. Cartagena's Old Town is a Unesco World Heritage site – a maze of cobbled alleys, balconies covered in bougainvillea, and massive churches that cast their shadows across leafy plazas. \nContinue reading on https://www.lonelyplanet.com/colombia/caribbean-coast/cartagena",
                "ims" : [
                    "https://i.pinimg.com/564x/67/28/78/672878b08a3395e91b0bb8cf9702ea59.jpg",
                    "https://i.pinimg.com/564x/91/49/62/91496203bfb475dbdfb2745cc800192b.jpg",
                    "https://i.pinimg.com/564x/3a/75/82/3a7582dba2c37be0441642709e468401.jpg",
                    "https://i.pinimg.com/564x/3c/cd/a2/3ccda2ac830440d97bf12567dc4f0a5f.jpg",
                    "https://i.pinimg.com/564x/36/84/a3/3684a34c20a25da4ce318b453a72b3c9.jpg",
                    "https://i.pinimg.com/564x/8e/95/86/8e958652b3672a81ec46f79fd1560180.jpg",
                    "https://i.pinimg.com/564x/b6/00/12/b60012c1fb0436806fb9324ad2c83106.jpg",
                    "https://i.pinimg.com/564x/09/22/f9/0922f9637bbe79e1617825bd93254ed8.jpg",
                    "https://i.pinimg.com/564x/35/90/2b/35902b04760b0583a938d7ab2855519e.jpg"

                ]
            },
            {
                "name": "Cali",
                "id": 3,
                "image": "Cali.jpg",
                "vertical": "Cali_2.jpg",
                "price": 149999,
                "dpt": "La Capital Mundial de la Salsa",
                "info" : "While it may not have the looks to front the tourist brochure, Cali is the kind of place that provides all the substance. It's a hot, gritty city with a passion for life that draws you in and stays with you long after you leave town. \nContinue reading on https://www.lonelyplanet.com/colombia/southwest-colombia/cali ",
                "ims" : [
                    "https://media-cdn.tripadvisor.com/media/photo-s/01/57/79/c7/colombia.jpg",
                    "https://media-cdn.tripadvisor.com/media/photo-s/05/73/ee/91/mirador-sebastian-belalcazar.jpg",
                    "https://media-cdn.tripadvisor.com/media/photo-s/06/50/22/c9/getlstd-property-photo.jpg",
                    "https://media-cdn.tripadvisor.com/media/photo-s/02/59/6b/5f/cristo-rey.jpg",
                    "https://media-cdn.tripadvisor.com/media/photo-s/01/c3/de/08/the-place.jpg"
                ]
            },
            {
                "name": "Medellín",
                "id": 4,
                "image": "Medellin.jpg",
                "vertical": "Medellin_2.jpg",
                "price": 189999,
                "dpt": "La Ciudad de la Eterna Primavera",
                "info" : "Medellín packs the punch of a city twice its size. Situated in a narrow valley, its skyline reaches for the heavens, setting high-rise apartment and office buildings against a backdrop of jagged peaks in every direction. Its pleasant climate gives it its nickname – the City of Eternal Spring – and the moderate temperatures put a spring in the locals' steps, at work and at play. It's a bustling place of industry and commerce, especially textile manufacturing and exported cut flowers. On weekends Medellín lets its hair down, its many discos attracting the beautiful people. \nContinue reading on https://www.lonelyplanet.com/colombia/northwest-colombia/medellin",
                "ims" : [
                    "https://i.pinimg.com/564x/03/14/2b/03142b0032304db6885ea105a63b5f4e.jpg",
                    "https://i.pinimg.com/564x/d1/ed/7d/d1ed7d71fa96b540d4f99c3b8c7a8c35.jpg",
                    "https://i.pinimg.com/564x/db/9d/c5/db9dc5bd4b07a9e2ba3cf59aeb149654.jpg",
                    "https://i.pinimg.com/564x/3f/7e/35/3f7e35aafb0c2caced725dd052ead723.jpg",
                    "https://i.pinimg.com/564x/8a/4e/c3/8a4ec3f2f5ac477ca86dc93820aba14a.jpg",
                    "https://i.pinimg.com/564x/bf/c6/1d/bfc61d04639550e321bd887747d78698.jpg",
                    "https://i.pinimg.com/564x/86/9d/f2/869df2a7351c242021ceb2525d8d24c5.jpg"

                ]
            },
            {
                "name": "Santa Marta",
                "id": 5,
                "image": "SantaMarta.jpg",
                "vertical": "SantaMarta_2.jpg",
                "price": 299999,
                "dpt": "La Perla de América",
                "info" : "Santa Marta is South America's oldest European-founded town and the second most important colonial city on Colombia's Caribbean coast. Despite its long history and charming center, it gets a bad rap from many travelers, who rightly cite its unsightly urban sprawl and terrible traffic as reasons not to hang about here. The secret to Santa Marta is to use it for what it does well: hotels, restaurants and bars, and then get out to the slew of superb destinations nearby during the daytime. \nContinue reading on https://www.lonelyplanet.com/colombia/caribbean-coast/santa-marta",
                "ims": [
                    "https://i.pinimg.com/564x/39/23/8f/39238fbf3920259dae78c4edf4db67da.jpg",
                    "https://i.pinimg.com/564x/b0/0b/d9/b00bd9cc3263ec13c38d0e06076872ca.jpg",
                    "https://i.pinimg.com/564x/ad/e2/bf/ade2bf1075c1ff5a5b3eb7e81fbe9bb2.jpg",
                    "https://i.pinimg.com/564x/4d/25/69/4d25694c558375a0ab1f245f6bcf5750.jpg",
                    "https://media-cdn.tripadvisor.com/media/photo-s/00/1b/22/f6/a-look-at-the-wonderful.jpg"
                ]
            },
            {
                "name": "Barranquilla",
                "id": 6,
                "image": "Barranquilla.jpg",
                "vertical": "Barranquilla_2.jpg",
                "price": 139999,
                "dpt": "La Puerta de Oro",
                "info" : "Barranquilla, Colombia's fourth-largest city, is a hardworking port town located on the delta of the massive River Magdalena and laid out in a tangled ribbon along mangroves and the Caribbean Sea, sweltering and hustling in the blinding sun. The birthplace of Colombian pop goddess Shakira, Barranquilla is actually most famous for its annual carnaval, when the town clocks off, puts on its glad rags and goes wild as it throws the country's biggest street party. \nContinue reading on https://www.lonelyplanet.com/colombia/barranquilla",
                "ims": [
                    "https://i.pinimg.com/564x/a5/cc/c8/a5ccc85e6490ca54214909a3c4eee0ab.jpg",
                    "https://i.pinimg.com/564x/15/ff/ed/15ffedc38f95c9d78272db556c38fdc0.jpg",
                    "https://i.pinimg.com/564x/82/00/47/820047fc75037fc8f25ea5d6806169ac.jpg",
                    "https://i.pinimg.com/564x/2b/f9/83/2bf983d53eaa7f84cdf216a37cbc8772.jpg",
                    "https://i.pinimg.com/564x/ef/8f/d9/ef8fd94eec833b60dad813f2cf2a960a.jpg",
                    "https://i.pinimg.com/564x/fd/d2/be/fdd2be145bf1870edb0fbe82a3ad78c4.jpg"

                ]
            },
            {
                "name": "Guaduas",
                "id": 8,
                "image": "Guaduas.jpg",
                "vertical": "Guaduas_2.jpg",
                "price": 19999,
                "dpt": "Villa de San Miguel de Guaduas",
                "info" : "Guaduas is a town in Colombia, in the Lower Magdalena Province department of Cundinamarca, about 117 km from Bogotá. It is an agricultural and tourist center of some importance with a population of about 33,000. Its name refers to a type of bamboo cane. It is one of the cities on the Bogotá-Medellín highway. Its main plaza is featured on the Colombian ten-thousand pesos bill, and is one of the seats of the Roman Catholic Diocese of La Dorada–Guaduas",
                "ims": [
                    "https://media-cdn.tripadvisor.com/media/photo-s/11/57/9f/58/torrentismo-en-guaduas.jpg",
                    "https://media-cdn.tripadvisor.com/media/photo-s/11/57/9d/db/el-mejor-clima-el-mejor.jpg",
                    "https://media-cdn.tripadvisor.com/media/photo-s/0e/58/6b/24/uitzicht-op-salto-de.jpg"
                ]
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


    




    