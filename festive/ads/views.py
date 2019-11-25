from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Location,Detail,images,Venue,VenuePrice,Dish_Menu
from users import views as users_views
from django.contrib import messages
from django.contrib.gis.geoip2 import GeoIP2
# Create your views here.

def display(request, id):

    featured_details = Detail.objects.filter(featured=True)
    featured_details_images   = {}
    featured_details_paarize  = {}

    
    for detail in featured_details:
        featured_details_images[detail.id] = images.objects.filter(detail_id=detail).first()
        featured_details_paarize[detail.id] = str(Dish_Menu.objects
        .get(venue_id = Venue.objects.get(detail_id = detail.id)))

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
       'featured_details':featured_details,
       'featured_details_images':featured_details_images,
       'featured_details_paarize':featured_details_paarize,
    }
    return render(request,"display.html", context)
def search(request, category, city,  min_price, max_price):
    venuePrice = VenuePrice.objects.filter(per_guest__gte=min_price)
    dic = {}     
    if category == 'None':
        if city == 'None':
            if max_price == '0':
                detail = Detail.objects.all()
                for deta in detail:
                    dic[deta.id] = deta
                context = {
                    'det' : dic,
                }
                return render(request,"search.html",context)
            else:
                for ven in venuePrice:
                    new=int(max_price)-ven.per_guest
                    dishMenu = Dish_Menu.objects.get(venue_id=ven.venue_id.id)
                    if new > dishMenu.price:
                        venue = Venue.objects.get(id=dishMenu.venue_id.id)
                        dic[ven.venue_id.detail_id.id] = Detail.objects.get(id=venue.detail_id.id)
                
                context = {
                    'det' : dic,
                }
                return render(request,"search.html",context)  
        else:
            if max_price == '0':
                print('ssssssssssss')
                location = Location.objects.filter(city=city)
                detail = Detail.objects.get(loction_id=location.id)
                context = {
                    'details' : detail,
                }
                return render(request,"search.html",context)
            else: 
                for ven in venuePrice:
                    new=int(max_price)-ven.per_guest
                    dishMenu = Dish_Menu.objects.get(venue_id=ven.venue_id.id)
                    if new > dishMenu.price:
                        venue = Venue.objects.get(id=dishMenu.venue_id.id)
                        if ven.venue_id.detail_id.loction_id.city == city:
                            dic[ven.venue_id.detail_id.id] = Detail.objects.get(id=venue.detail_id.id)
                context = {
                    'det' : dic,
                }
                return render(request,"search.html",context)
    else:    
        if city == 'None':
            if max_price == '0':
                venue = Venue.objects.filter(category=category)
                detail = Detail.objects.filter(id=venue.detail_id)
                context = {
                    'venues':venue,
                }
                return render(request,"search.html",context)
            else:
                for ven in venuePrice:
                    new=int(max_price)-ven.per_guest
                    dishMenu = Dish_Menu.objects.get(venue_id=ven.venue_id.id)
                    if new > dishMenu.price:
                        venue = Venue.objects.get(id=dishMenu.venue_id.id)
                        if venue.category == category:
                            dic[ven.venue_id.detail_id.id] = Detail.objects.get(id=venue.detail_id.id)     
                context = {
                    'det' : dic,
                }
                return render(request,"search.html",context)  
        else:
            if max_price == '0':
                location = Location.objects.filter(city=city)
                detail = Detail.objects.get(loction_id=location.id)
                context = {
                        'details' : detail,
                }
                return render(request,"search.html",context)
            else:
                for ven in venuePrice:
                    new=int(max_price)-ven.per_guest
                    dishMenu = Dish_Menu.objects.get(venue_id=ven.venue_id.id)
                    if new > dishMenu.price:
                        venue = Venue.objects.get(id=dishMenu.venue_id.id)
                        if venue.category == category:
                            if ven.venue_id.detail_id.loction_id.city == city:
                                dic[ven.venue_id.detail_id.id] = Detail.objects.get(id=venue.detail_id.id)
                context = {
                    'det' : dic,
                }
                return render(request,"search.html",context)

def main(request):

    g = GeoIP2()
    if request.META.get('HTTP_X_FORWARDED_FOR'):
        ip_address = request.META.get('HTTP_X_FORWARDED_FOR')
        print("XFWD: ", ip_address)
    elif request.META.get('REMOTE_ADDR'):
        ip_address = request.META.get('REMOTE_ADDR')
        print("RMT: ", ip_address)
    
    if ip_address == '127.0.0.1':
        city = 'Lahore'
        print('IP: 27')
    else:
        city = g.city(ip_address)['city']
        if not city:
            city = 'Lahore'

    featured_details = Detail.objects.filter(featured=True)
    featured_details_images   = {}
    featured_details_paarize  = {}

    
    for detail in featured_details:
        featured_details_images[detail.id] = images.objects.filter(detail_id=detail).first()
        featured_details_paarize[detail.id] = str(Dish_Menu.objects
        .filter(venue_id = Venue.objects.get(detail_id = detail.id)).first())
    

    locs = Location.objects.filter(city='Lahore')[:8]
    loc_based_details = {}
    loc_based_images = {}
    loc_based_prices = {}
    
    for loc in locs:
        loc_based_details[Detail.objects.get(loction_id=loc).id] = Detail.objects.get(loction_id=loc)
        loc_based_images[Detail.objects.get(loction_id=loc).id] = images.objects.filter(detail_id=
                Detail.objects.get(loction_id=loc).id).first()
        loc_based_prices[Detail.objects.get(loction_id=loc).id] = str(Dish_Menu.objects
        .get(venue_id = Venue.objects.get(detail_id = Detail.objects.get(loction_id=loc).id)))
    



    context = {
        'featured_details' : featured_details,
        'featured_details_images': featured_details_images,
        'featured_details_paarize': featured_details_paarize,
        'loc_based_details': loc_based_details,
        'loc_based_images': loc_based_images,
        'loc_based_prices' : loc_based_prices,
        'location' : 'Lahore',
    }

    if request.method == 'POST':
        category = request.POST.get('category')
        city =request.POST.get('city')
        min_price = 100
        max_price = 0
        return redirect(search, category, city, min_price, max_price)
    else:
        return render(request,"main.html", context)

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

def add(request):
    if request.user.is_authenticated:
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
            
            
            #for venue
            sitting_capacity =request.POST.get('sitting_capacity')
            category = request.POST.get('category')
            parking_capacity =request.POST.get('parking_capacity')
            heater = request.POST.get('heater')
            ac = request.POST.get('ac')
            dj_system = request.POST.get('dj_system')
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
        
            location = Location.objects.create(city=city, area=area, street=street)
            detail = Detail.objects.create(title=post_title, loction_id=location, phoneNo=phone, 
                featured=feature, description=post_description, rating=rating, views=views)
            
            for img in request.FILES.getlist('images'):
                image = images.objects.create(title=post_title, detail_id=detail, image=img)
            venue = Venue.objects.create(author=request.user, detail_id=detail, sitting_capacity=sitting_capacity, 
                parking_capacity=parking_capacity) 
            VenuePrice.objects.create(venue_id=venue, per_guest=guest_price, air_conditioner=ac_price, heater=heater_price, 
                dj_system=dj_system_price, decoration=decoration_price)
            
            # for dish menu
            leng = request.POST.get('menu')
            leng= int(leng)+1
            if request.POST:
                i = 1
                for index in range(i,leng):
                    print(index)
                    dish_title =""
                    dish_description =""
                    price =""
                    flag=0
                    if 'dish_title'+str(index) in request.POST:
                        dish_title= request.POST['dish_title'+str(index)]
                        flag = 1
                    if 'dish_description'+str(index) in request.POST:
                        dish_description= request.POST['dish_description'+str(index)]
                        flag = 1
                    if 'price'+str(index)  in request.POST:
                        price= request.POST['price'+str(index)]         
                        flag = 1

                    if flag == 1: 
                        print('sssss')
                        Dish_Menu.objects.create(venue_id=venue, title=dish_title, description=dish_description, price=price)
            return redirect('/')

        else:
            return render(request,'add.html')
    else:
        messages.error(request, 
            "You have to login first to post an Ad.",
            extra_tags="message")
        return redirect(users_views.login)

