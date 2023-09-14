from django.http import HttpResponse
from django.shortcuts import render
from .models import Menu
from django.core import serializers
from .models import Booking
from datetime import datetime
import json
from django.http import JsonResponse, HttpResponse
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

# def bookings(request):
#     date = request.GET.get('date', datetime.today().date())
#     bookings = Booking.objects.all()
#     booking_json = serializers.serialize('json', bookings)
#     return render(request, 'bookings.html', {'bookings': booking_json})

@csrf_exempt
def bookings_get(request):
    try:
        if request.method == 'GET':
            date = request.GET.get("date", datetime.today().date())
            bookings = Booking.objects.all().filter(reservation_date=date)
            booking_list = list(bookings.values())
            return JsonResponse({'data': booking_list}, safe=False)
        elif request.method == 'POST':
            print("Received POST request.")
            bookings_post(request)
            return HttpResponse(status=200)
        else:
            print("Unhandled HTTP method.")
            return HttpResponse(status=405)
    except Exception as e:
        # Log the exception for debugging
        print(f"Error occurred: {e}")
        return HttpResponse(status=500)

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
def bookings_post(request):
    try: 
        if request.method == 'POST':
            print("Inside bookings_post function")
            data = json.loads(request.body.decode("utf-8"))
            print("Received Data: ", data)
            
            # Check if the reservation_slot key exists in the data
            if 'reservation_slot' not in data:
                print("Missing reservation_slot")
                return JsonResponse({'error': 'Missing reservation_slot'}, status=400)

            exist = (
                Booking.objects.filter(reservation_date=data["reservation_date"])
                .filter(reservation_slot=data["reservation_slot"])
                .exists()
            )
            if not exist:
                print("No existing reservation found for this slot and date.")
                booking = Booking(
                    first_name=data["first_name"],
                    reservation_date=data["reservation_date"],
                    reservation_slot=data["reservation_slot"],
                )
                booking.save(force_insert=True)
                print("Booking saved!")
                return HttpResponse(status=200)
            else:
                print("Existing reservation found.")
                return HttpResponse("{'error':1}", content_type="application/json")
    except Exception as e:
        print(f"Exception in bookings_post: {e}")
        return HttpResponse(status=500)
    
    date = request.GET.get("date", datetime.today().date())
    bookings = Booking.objects.all().filter(reservation_date=date)
    booking_list = list(bookings.values())
    # booking_json = serializers.serialize("json", bookings)
    print(f"Received date: {date}")
    print(f"Bookings Query Result: {bookings}")

    # return JsonResponse(booking_json, safe=False)
    return JsonResponse({'data': booking_list}, safe=False)