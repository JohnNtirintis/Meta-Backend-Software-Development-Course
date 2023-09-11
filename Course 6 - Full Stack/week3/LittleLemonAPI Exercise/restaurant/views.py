from django.http import HttpResponse
from django.shortcuts import render
from .models import Menu
from django.core import serializers
from .models import Booking
from datetime import datetime
import json
from django.http import JsonResponse
from .forms import BookingForm
from django.views.decorators.csrf import csrf_exempt

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'book.html', context)

def bookings(request):
    date = request.GET.get('date', datetime.today().date())
    bookings = Booking.objects.all()
    booking_json = serializers.serialize('json', bookings)
    return render(request, 'bookings.html', {'bookings': booking_json})

def menu(request):
    menu_data = Menu.objects.all()
    main_data = {"menu": menu_data}
    return render(request, 'menu.html', {"menu": main_data})


def display_menu_item(request, pk=None): 
    if pk: 
        menu_item = Menu.objects.get(pk=pk) 
    else: 
        menu_item = "" 
    return render(request, 'menu_item.html', {"menu_item": menu_item}) 

@csrf_exempt
def bookings(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))  # Notice that it should be json.loads() not json.load()

        # Check if the reservation_slot key exists in the data
        if 'reservation_slot' not in data:
            return JsonResponse({'error': 'Missing reservation_slot'}, status=400)

        exist = (
            Booking.objects.filter(reservation_date=data["reservation_date"])
            .filter(reservation_slot=data["reservation_slot"])
            .exists()
        )
        if not exist:
            booking = Booking(
                first_name=data["first_name"],
                reservation_date=data["reservation_date"],
                reservation_slot=data["reservation_slot"],
            )
            booking.save()
        else:
            return HttpResponse("{'error':1}", content_type="application/json")
    
    date = request.GET.get("date", datetime.today().date())
    bookings = Booking.objects.all().filter(reservation_date=date)
    booking_list = list(bookings.values())
    # booking_json = serializers.serialize("json", bookings)
    print(f"Received date: {date}")
    print(f"Bookings Query Result: {bookings}")

    # return JsonResponse(booking_json, safe=False)
    return JsonResponse({'data': booking_list}, safe=False)