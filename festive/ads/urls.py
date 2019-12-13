from django.urls import path,include
from . import views
# from rest_framework import routers

# router = routers.DefaultRouter()
# router.register('record',views.recordList)

urlpatterns = [
    # path('route',include(router.urls)),
    path('',views.main, name='festive-circle'),
    path('add-venue',views.add, name='add'),
    path('search/q=ca_<category>&ct_<city>&min-pr_<min_price>&max-pr_<max_price>',views.search, name='search'),
    path('venue/<id>/',views.display,name='display'),
    path('edit/<id>/',views.edit,name='edit'),
    path('delete/<id>/',views.delete,name='delete'),

    # path('main/<id>/',views.delete,name='delete'),
    # path('record/json/',views.json,name='json'),


]
