from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
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
    
    featured_details = Detail.objects.filter(featured=True)
    featured_details_images   = {}
    featured_details_paarize  = {}

    
    for detail in featured_details:
        featured_details_images[detail.id] = images.objects.filter(detail_id=detail).first()
        featured_details_paarize[detail.id] = str(Dish_Menu.objects
        .get(venue_id = Venue.objects.get(detail_id = detail.id)))
    


    top_4_popular_details = Detail.objects.all().order_by('-views')[:4]
    top_4_popular_details_images   = {}
    top_4_popular_details_paarize  = {}

    for detail in top_4_popular_details:
        top_4_popular_details_images[detail.id]   = images.objects.filter(detail_id=detail).first()
        top_4_popular_details_paarize[detail.id] = str(Dish_Menu.objects
        .get(venue_id = Venue.objects.get(detail_id = detail.id)))

    print("pop ", top_4_popular_details_paarize)
    print("featured ", featured_details_paarize)

    
    context = {
        'featured_details' : featured_details,
        'featured_details_images': featured_details_images,
        'featured_details_paarize': featured_details_paarize,
        'top_4_popular_details': top_4_popular_details,
        'top_4_popular_details_images': top_4_popular_details_images,
        'top_4_popular_details_paarize' : top_4_popular_details_paarize,
    }

    if request.method == 'POST':
        category = request.POST.get('category')
        city =request.POST.get('city')
        area =request.POST.get('Area')
        if category is None:
            if city is None:
                return redirect('/')
            else:
                if area is None:
                    location = Location.objects.filter(city=city)
                    detail = Detail.objects.all()
                    context = {
                        'details':detail,
                        'locations':location,
                    }
                    return render(request,"search.html",context)


                else:
                    location = Location.objects.filter(city=city)
                    location = location.filter(area=area)                   
                    detail = Detail.objects.all()
                    context = {
                        'details':detail,
                        'locations':location,
                    }
                    return render(request,"search.html",context)
        else:
            if city is None:
                venue = Venue.objects.filter(category=category)
                context = {
                    'venues':venue,
                }
                return render(request,"search.html",context)
            else:
                if area is None:
                    location = Location.objects.filter(city=city)
                    venue = Venue.objects.filter(category=category)
                    context = {
                        'venues':venue,
                        'locations':location,
                    }
                    return render(request,"search.html",context)
                else:
                    location = Location.objects.filter(city=city)
                    location = location.filter(area=area)
                    venue = Venue.objects.filter(category=category)
                    context = {
                        'venues':venue,
                        'locations':location,
                    }
                    return render(request,"search.html",context)


        return redirect('/')
    else:
        return render(request,"main.html",context)

def edit(request, id):

    detail = Detail.objects.get(id=id)
    # loc = Location.objects.get(id=detail.loction_id.id)
    # print(loc.id)
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


        Location.objects.filter(id=id).update(city=city, area=area, street=street)
        
        Detail.objects.filter(id=id).update(title=post_title,phoneNo=phone,description=post_description)
        for img in request.FILES.getlist('images'):
            images.objects.filter(detail_id=id).update(title=post_title,image=img)
        Venue.objects.filter(detail_id=id).update(sitting_capacity=sitting_capacity,category=category,parking_capacity=parking_capacity,air_conditioner=ac,heater=heater,dj_system=dj_system,wifi=wifi,bridal_room=bridal_room,valet_parking=valet_parking,decoration=decoration,generator=generator,outside_catering=outside_catering,outside_dj=outside_dj,outside_decoration=outside_decoration)
        VenuePrice.objects.filter(venue_id=venue).update(per_guest=guest_price,air_conditioner=ac_price,heater=heater_price,dj_system=dj_system_price,decoration=decoration_price)
        Dish_Menu.objects.filter(venue_id=venue).update(title=dish_title,description=dish_description,price=price)
        
        print('post update')
        return redirect('/')

    else:
        return render(request,"edit.html", context)

def delete(request,id):
    location = Location.objects.get(id=id)
    if request.method == 'POST':
        location.delete()
        return redirect('/')
    return render(request,'delete.html')

# @login_required
def add(request):
    if request.method == 'POST':
        
        #for detail
        post_title =request.POST.get('post_title')
        phone =request.POST.get('phone')
        
        if request.POST.get('feature') == 'on':
            feature = True
        else:
            feature = False
        
        post_description =request.POST.get('post_description')
        rating = request.POST.get('rating')
        views = request.POST.get('views')

        #for location
        city =request.POST.get('city')
        area =request.POST.get('area')
        street =request.POST.get('street')


        #for dish menu
        dish_title =request.POST.get('dish_title')
        dish_description =request.POST.get('dish_description')
        price =request.POST.get('price')
        
        
        #for venue
        sitting_capacity =request.POST.get('sitting_capacity')
        category = request.POST.get('category')
        parking_capacity =request.POST.get('parking_capacity')
        heater =request.POST.get('heater')
        ac =request.POST.get('ac')
        dj_system =request.POST.get('dj_system')
        wifi =request.POST.get('wifi')
        valet_parking =request.POST.get('valet_parking')
        bridal_room =request.POST.get('bridal_room')
        generator =request.POST.get('generator')
        outside_dj =request.POST.get('outside_dj')
        outside_decoration =request.POST.get('outside_decoration')
        outside_catering =request.POST.get('outside_catering')
        decoration =request.POST.get('decoration')    

        #for venue price
        guest_price =request.POST.get('guest_price')
        ac_price =request.POST.get('ac_price')
        heater_price =request.POST.get('heater_price')
        dj_system_price =request.POST.get('dj_system_price')
        decoration_price =request.POST.get('decoration_price')
       


        
        
        # print(post_title, rating, views,
        # feature, phone, city, area, street, images, post_description)
        # print(guest_price, ac_price, heater_price, dj_system_price,
        # decoration_price)
        # print(dish_title, dish_description, price, sitting_capacity,
        # parking_capacity, category )

        location = Location.objects.create(city=city, area=area, street=street)
        detail = Detail.objects.create(title=post_title, loction_id=location, phoneNo=phone, 
            featured=feature, description=post_description, rating=rating, views=views)
        
        for img in request.FILES.getlist('images'):
            image = images.objects.create(title=post_title, detail_id=detail, image=img)
        print("cat ", category)
        venue = Venue.objects.create(author=request.user, detail_id=detail, sitting_capacity=sitting_capacity, 
            parking_capacity=parking_capacity) 
        # air_conditioner=ac, heater=heater, 
        # dj_system=dj_system, wifi=wifi, bridal_room=bridal_room, valet_parking=valet_parking, 
        # decoration=decoration, generator=generator, outside_catering=outside_catering, 
        # outside_dj=outside_dj, outside_decoration=outside_decoration)
        VenuePrice.objects.create(venue_id=venue, per_guest=guest_price, air_conditioner=ac_price, heater=heater_price, 
            dj_system=dj_system_price, decoration=decoration_price)
        Dish_Menu.objects.create(venue_id=venue, title=dish_title, description=dish_description, price=price)
        return redirect('/')

    else:
        return render(request,'add.html')

