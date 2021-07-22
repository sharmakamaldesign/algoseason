from django.urls import path,include    
from . import views


app_name = 'authentication'

urlpatterns = [
    path('login/',views.userLogin,name='login'),
    path('sign_up/',views.signUp,name='sign_up'),
    path('logout/',views.logout,name='logout'),
    # path('handlerequest/',views.handlerequest,name='handlerequest'),
]