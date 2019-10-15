from django.shortcuts import render
from .models import Location,Detail,images,Venue,VenuePrice,Dish_Menu

# Create your views here.
def main(request):
    return render(request,"main.html")

def add(request):
    if request.method == 'POST':
        post_title =request.POST.get['post_title']
        phone =request.POST.get['phone']
        city =request.POST.get['city']
        area =request.POST.get['area']
        street =request.POST.get['street']
        image =request.POST.get['image']
        post_description =request.POST.get['post_description']
        guest_price =request.POST.get['guest_price']
        ac_price =request.POST.get['ac_price']
        heater_price =request.POST.get['heater_price']
        dj_system_price =request.POST.get['dj_system_price']
        decoration_price =request.POST.get['decoration_price']
        dish_title =request.POST.get['dish_title']
        dish_description =request.POST.get['dish_description']
        price =request.POST.get['price']
        sitting_capacity =request.POST.get['sitting_capacity']
        parking_capacity =request.POST.get['parking_capacity']
        decoration =request.POST.get['decoration']
        wifi =request.POST.get['wifi']
        valet_parking =request.POST.get['valet_parking']
        heater =request.POST.get['heater']
        ac =request.POST.get['ac']
        dj_system =request.POST.get['dj_system']
        bridal_room =request.POST.get['bridal_room']
        generator =request.POST.get['generator']
        outside_dj =request.POST.get['outside_dj']
        outside_decoration =request.POST.get['outside_decoration']

        


        Loction = loction.objects.create(city=city,area=area,street=street)
        Detail = Detail.objects.create(title=post_title,loction_id=Loction,phoneNo=phone,description=post_description)
        for img in image:
            image = images.objects.create(title=post_title,detail_id=Detail,image=image)
        
        print('post add')
        return redirect('')

    else:
        return render(request,'add.html')

