from django.contrib import admin
from .models import Order, PromoCode
# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_id','price','order_date','txn_amount','is_payment_successful']

class PromoCodeAdmin(admin.ModelAdmin):
    list_display = ['id','promo_code','discount_in_percent','created_date','expiry_date']

admin.site.register(Order, OrderAdmin)
admin.site.register(PromoCode, PromoCodeAdmin)