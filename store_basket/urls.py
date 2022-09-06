from . import views
from django.urls import path

app_name = "store_basket"

urlpatterns = [
    path('', views.basket_summary,name='basket_summary'),
    path('',views.basket_add,name='basket_add')

]


