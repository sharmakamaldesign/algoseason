from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    # path('',views.home,name='home'),
    path('order_details/',views.order_details, name='order_details'),
    path('purchase/',views.purchase, name='purchase'),
    path('handle_payment_request/',views.handlePaymentRequest, name='handle_payment_request'),
    # path('order-status/',views.orderStatus(), name='order_status'),

]