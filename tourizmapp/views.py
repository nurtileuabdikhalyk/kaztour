import requests
from django.shortcuts import render

from .models import *


def home(request):
    try:
        city = Citys.objects.all()
    except KeyError:
        pass

    params = {
        'path': request.path.split('/')[1],
        'city': city,
    }
    # Hotel.objects.all().delete()

    # df = pd.read_pickle(r'baza_hotels1.pkl')
    # df_records = df.to_dict('records')

    # model_instances = [Hotel(
    #     name = record['title'],
    #     city = record['city'],
    #     img = record['img'],
    #     price = record['price1'],
    #     price_usd = record['price_d'],
    #     price_rus = record['price_r'],
    #     price_eur = record['price_e'],

    # ) for record in df_records]

    # Hotel.objects.bulk_create(model_instances)

    if request.method == 'GET':
        try:
            requ = Requests()
            requ.name = request.GET['name']
            requ.phone_number = request.GET['number']
            requ.hotel = request.GET['hotel']
            requ.child = int(request.GET['child'])
            requ.adult = int(request.GET['adult'])
            requ.date1 = request.GET['date_in']
            requ.date2 = request.GET['date_out']

            requ.cardholder_name = request.GET['cardholder-name']
            requ.card_number = request.GET['card-number']
            requ.expiration_date = request.GET['expiration-date']
            requ.cvc = request.GET['cvc']
            requ.save()

            return render(request, 'index.html')
        except Exception as e:
            print(str(e))
    else:
        print("DCDC")

    if request.method == 'GET':
        try:
            message = Message()
            message.name = request.GET['name']
            message.email = request.GET['email']
            message.text = request.GET['message']
            message.subject = request.GET['subject']
            message.save()
        except Exception as e:
            print(str(e))

    return render(request, 'index.html', params)


def get_weather(city):
    api_key = "302d9605c5b48be11c18b3682dcc8dc4"
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        response = requests.get(url)
        data = response.json()
        weather = {
            "description": data["weather"][0]["description"],
            "temperature": round(data["main"]["temp"] - 273.15, 1),
            "humidity": data["main"]["humidity"],
            "icon": f"http://openweathermap.org/img/w/{data['weather'][0]['icon']}.png",
        }
    except:
        city = 'Алматы'
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        response = requests.get(url)
        data = response.json()
        weather = {
            "description": data["weather"][0]["description"],
            "temperature": round(data["main"]["temp"] - 273.15, 1),
            "humidity": data["main"]["humidity"],
            "icon": f"http://openweathermap.org/img/w/{data['weather'][0]['icon']}.png",
        }

    return weather


def country(request):
    # Requests(request)

    try:
        name_objects = request.GET['id']
        items = Citys.objects.filter(name=name_objects)
    except KeyError:
        items = Citys.objects.filter(id=1)

    try:
        name_objects = request.GET['id']
        hotels = Hotel.objects.filter(city=name_objects)
    except KeyError:
        hotels = Hotel.objects.filter(id=1)

    try:
        city = Citys.objects.all()
    except KeyError:
        pass

    for item in items:
        pass

    cur_city = item.name  # или получите город из GET-параметра запроса
    weather_data = get_weather(cur_city)

    import datetime

    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")

    params = {
        'item': item,
        'hotels': hotels,
        'city': city,
        "weather": weather_data,
        'path': request.path.split('/')[1],
        'current_time': current_time
    }

    return render(request, 'country.html', params)


def request(request):
    name_objects = request.GET['id']

    try:
        city = Citys.objects.all()
    except KeyError:
        pass

    params = {
        'city': city,
        'path': request.path.split('/')[1],
        'name_objects': name_objects
    }

    return render(request, 'reviews.html', params)


def contact(request):
    # Message.objects.all().delete()

    try:
        city = Citys.objects.all()
    except KeyError:
        pass

    params = {
        'city': city,
        'path': request.path.split('/')[1],
    }

    return render(request, 'contact.html', params)


def tourist_spot(request):
    tours = TourObjects.objects.all()
    city = Citys.objects.all()
    context = {
        'tours': tours,
        'path': request.path.split('/')[1],
        'city': city
    }
    return render(request, 'tourobjects.html', context)


def tourist_spot_detail(request, pk):
    tour = TourObjects.objects.get(id=pk)
    city = Citys.objects.all()
    objectsDetails = ObjectsDetail.objects.filter(tourobjects=tour)
    context = {
        'objectsDetails': objectsDetails,
        'tour': tour,

        'path': request.path.split('/')[1],
        'city': city
    }
    return render(request, 'tourist_spot_detail.html', context)


def object_detail(request, pk):
    objectDetail = ObjectsDetail.objects.get(id=pk)
    city = Citys.objects.all()
    context = {
        'objectDetail': objectDetail,
        'path': request.path.split('/')[1],
        'city': city
    }
    return render(request, 'objectDetail.html', context)


def guide(request):
    request_city = ''
    request_language = ''
    if request.method == 'POST':

        request_city = str(request.POST['city'])
        request_language = str(request.POST['language'])

        if request_city == 'Барлық':
            guides = Guide.objects.all()
        if request_language == 'Барлық':
            guides = Guide.objects.all()
        if request_city != 'Барлық':
            if request_language == 'Барлық':
                guides = Guide.objects.filter(city=request_city)
            else:
                guides = Guide.objects.filter(city=request_city).filter(language=request_language)
        if request_language != 'Барлық':
            if request_city == 'Барлық':
                guides = Guide.objects.filter(language=request_language)
            else:
                guides = Guide.objects.filter(city=request_city).filter(language=request_language)

    else:
        guides = Guide.objects.all()

    city = Citys.objects.all()
    context = {
        'request_city': request_city,
        'request_language': request_language,
        'guides': guides,
        'path': request.path.split('/')[1],
        'city': city
    }
    return render(request, 'guide.html', context)
