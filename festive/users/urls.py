from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views
from .views import (login, register_request, 
logout_request, password_reset_request, match_code_request,
new_password_request, home, change_password_request, update_profile_request)
from django.conf import settings
from django.conf.urls.static import static # new


urlpatterns = [
    path('home/', home, name='home'),
    path('login/', login, name='login'),
    path('register/', register_request, name='register'),
    path('logout/', logout_request, name='logout'),
    path('recover/', password_reset_request, name='recoverpassword'),
    path('emailcode/', match_code_request, name='emailcode'),
    path('newpass/', new_password_request, name='newpassword'),
    path('changepassword/', change_password_request, name='changepassword'),
    path('updateprofile/', update_profile_request, name='updateprofile'),

]

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
