from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Order(models.Model):
	order_id = models.AutoField(primary_key=True)
	price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
	is_payment_successful = models.BooleanField(default=False)
	order_date = models.DateTimeField(auto_now_add=True)
	bank_txn_id = models.CharField(max_length=250, null=True, blank=True)
	txn_date = models.DateTimeField(blank=True, null=True)
	txn_id = models.CharField(max_length=250,null=True, blank=True)
	txn_status = models.CharField(max_length=250, null=True, blank=True)
	txn_gate_way_name = models.CharField(max_length=250, null=True, blank=True)
	txn_bank_name = models.CharField(max_length=250, null=True, blank=True)
	txn_response_code = models.IntegerField(null=True, blank=True)
	txn_payment_mode = models.CharField(max_length=250, null=True, blank=True)
	txn_response_message = models.CharField(max_length=250, null=True, blank=True)
	txn_currency = models.CharField(max_length=250, null=True, blank=True)
	txn_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
	promo_code = models.CharField(max_length=250, null=True, blank=True)
	promo_code_discount_in_percent = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
	user = models.ForeignKey(User,on_delete=models.CASCADE)

	class Meta:
		db_table='Order'
		# ordering = ['-created']
		
	def __str__(self):
		return str(self.order_id)
	
class PromoCode(models.Model):
	promo_code = models.CharField(max_length=250, blank=True, unique=True)
	discount_in_percent = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
	created_date = models.DateTimeField(auto_now_add=True)
	expiry_date = models.DateTimeField(blank=True, null=True)

	class Meta:
		db_table='PromoCode'
		# ordering = ['-created']
		
	def __str__(self):
		return str(self.id)
	