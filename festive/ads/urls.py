from django.urls import path,include
from . import views
# from rest_framework import routers

# router = routers.DefaultRouter()
# router.register('record',views.recordList)

urlpatterns = [
    # path('route',include(router.urls)),
    path('',views.main, name='festive-circle'),
    path('add',views.add, name='add-venue'),
    # path('edit/<id>/',views.edit,name='edit'),
    # path('main/<id>/',views.delete,name='delete'),
    # path('record/json/',views.json,name='json'),


]
