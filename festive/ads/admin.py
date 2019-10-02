from django.contrib import admin

# Register your models here.
from .models import Detail,Location,Venue,VenuePrice,images,Dish_Menu
admin.site.register(Detail)
admin.site.register(Location)
admin.site.register(Venue)
admin.site.register(VenuePrice)
admin.site.register(images)
admin.site.register(Dish_Menu)