from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Location,Detail,images,Venue,VenuePrice,Dish_Menu

# Create your views here.

def display(request, id):
    detail = Detail.objects.get(id=id)
    image = images.objects.filter(detail_id=id)
    venue = Venue.objects.get(detail_id=id)
    venuePrice = VenuePrice.objects.get(venue_id=venue)
    dishMenu = Dish_Menu.objects.get(venue_id=venue)
    context = {
       'details':detail,
       'images':image,
       'venues':venue,
       'venuePrices':venuePrice,
       'dishMenus':dishMenu,
    }
    return render(request,"display.html", context)
    
def main(request):
    detail = Detail.objects.all()
    location = Location.objects.all()
    context = {
        'details':detail,
        'locations':location,
    }
    if request.method == 'POST':
        category =request.POST.get('category')
        city =request.POST.get('city')
        Area =request.POST.get('Area')
        
        return redirect('/')
    else:
        return render(request,"main.html",context)

def edit(request, id):
    detail = Detail.objects.get(id=id)
    # location = Location.objects.get(id=detail.loction_id.id)
    image = images.objects.filter(detail_id=id)
    venue = Venue.objects.get(detail_id=id)
    venuePrice = VenuePrice.objects.get(venue_id=venue)
    dishMenu = Dish_Menu.objects.get(venue_id=venue)
    context = {
       'details':detail,
       'images':image,
       'venues':venue,
       'venuePrices':venuePrice,
       'dishMenus':dishMenu,
    }
    return render(request,"edit.html", context)

def delete(request,id):
    location = Location.objects.get(id=id)
    if request.method == 'POST':
        location.delete()
        return redirect('/')
    return render(request,'delete.html')


def add(request):
    if request.method == 'POST':
        post_title =request.POST.get('post_title')
        phone =request.POST.get('phone')
        city =request.POST.get('city')
        area =request.POST.get('area')
        street =request.POST.get('street')
        post_description =request.POST.get('post_description')
        guest_price =request.POST.get('guest_price')
        ac_price =request.POST.get('ac_price')
        heater_price =request.POST.get('heater_price')
        dj_system_price =request.POST.get('dj_system_price')
        decoration_price =request.POST.get('decoration_price')
        dish_title =request.POST.get('dish_title')
        dish_description =request.POST.get('dish_description')
        price =request.POST.get('price')
        sitting_capacity =request.POST.get('sitting_capacity')
        parking_capacity =request.POST.get('parking_capacity')
        decoration =request.POST.get('decoration')
        wifi =request.POST.get('wifi')
        valet_parking =request.POST.get('valet_parking')
        heater =request.POST.get('heater')
        ac =request.POST.get('ac')
        dj_system =request.POST.get('dj_system')
        bridal_room =request.POST.get('bridal_room')
        generator =request.POST.get('generator')
        outside_dj =request.POST.get('outside_dj')
        outside_decoration =request.POST.get('outside_decoration')
        outside_catering =request.POST.get('outside_catering')
        category = request.POST.get('category')

        


        location = Location.objects.create(city=city,area=area,street=street)
        detail = Detail.objects.create(title=post_title,loction_id=location,phoneNo=phone,description=post_description)
        for img in request.FILES.getlist('images'):
            image = images.objects.create(title=post_title,detail_id=detail,image=img)
        venue = Venue.objects.create(author=request.user,detail_id=detail,sitting_capacity=sitting_capacity,category=category,parking_capacity=parking_capacity,air_conditioner=ac,heater=heater,dj_system=dj_system,wifi=wifi,bridal_room=bridal_room,valet_parking=valet_parking,decoration=decoration,generator=generator,outside_catering=outside_catering,outside_dj=outside_dj,outside_decoration=outside_decoration)
        venuePrice = VenuePrice.objects.create(venue_id=venue,per_guest=guest_price,air_conditioner=ac_price,heater=heater_price,dj_system=dj_system_price,decoration=decoration_price)
        dish_Menu = Dish_Menu.objects.create(venue_id=venue,title=dish_title,description=dish_description,price=price)
        print('post add')
        return redirect('/')

    else:
        return render(request,'add.html')

