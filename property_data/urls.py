from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.property_form,name='property_insert'), #get and post request for insert operation
    path('<int:id>/',views.property_form,name='property_update'),#get and post request for update operation
    path('delete/<int:id>/',views.property_delete,name='property_delete'),
    path('list/', views.property_list,name='property_list'),# get request for list operation

    path('',views.activity_form,name='activity_insert'), #get and post request for insert operation
    path('<int:id>/',views.activity_form,name='activity_update'),#get and post request for update operation
    path('delete/<int:id>/',views.activity_delete,name='activity_delete'),
    path('list/', views.activity_list,name='activity_list'),# get request for list operation
]
