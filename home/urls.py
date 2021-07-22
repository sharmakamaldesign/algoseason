from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('',views.home,name='home'),
    path('pricing/',views.pricing, name='pricing'),
    path('contact_us/',views.contact_us, name='contact_us')

]