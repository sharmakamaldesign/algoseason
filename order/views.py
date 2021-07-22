from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from paytm import Checksum
from django.contrib.auth.decorators import login_required
from .models import Order
from user_profile import views as profile_views
# Create your views here.
BASE_URL = "192.168.1.65:8000"
MERCHANT_KEY = '9xUwl6__RaJx2w@e'

def order_details(request):
	return render(request,'order_details.html',{'course_price':399})
@login_required(login_url='authentication:login')
def purchase(request):
	order = Order.objects.create(user = request.user, price = 499)
	order_id = order.order_id
	param_dict = {
					'MID': 'KiaDJA62433482916699',
					'ORDER_ID': str(order_id),
					'TXN_AMOUNT': '399',
					'CUST_ID': str(request.user.id),
					'INDUSTRY_TYPE_ID': 'Retail',
					'WEBSITE': 'WEBSTAGING',
					'CHANNEL_ID': 'WEB',
					'CALLBACK_URL': 'http://'+BASE_URL+'/order/handle_payment_request/',
				}
	param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(
		param_dict, MERCHANT_KEY)
	return render(request, 'paytm.html', {'param_dict': param_dict})


@csrf_exempt
def handlePaymentRequest(request):
	# paytm will send you post request here.
	print("user id is ",request.user.id)
	form = request.POST
	response_dict = {}
	print("---------from ", form)
	for i in form.keys():
		print('----', i, '-----', form[i])
		response_dict[i] = form[i]
		if i == 'CHECKSUMHASH':
			checksum = form[i]

	varify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
	print("varifi is ", varify)
	if varify:
		order_object = Order.objects.get(order_id = response_dict['ORDERID']) 
		user = order_object.user
		order_object.amount = response_dict['TXNAMOUNT']
		order_object.txn_response_code = response_dict['RESPCODE']
		order_object.txn_response_message = response_dict['RESPMSG']
		order_object.txn_status = response_dict['STATUS']

		if response_dict['RESPCODE'] == '01':
			order_object.is_payment_successful = True
			order_object.bank_txn_id = response_dict['BANKTXNID']
			order_object.txn_bank_name = response_dict['BANKNAME']
			order_object.txn_date = response_dict['TXNDATE']
			order_object.txn_gate_way_name = response_dict['GATEWAYNAME']
			order_object.txn_id = response_dict['TXNID']
			order_object.txn_payment_mode = response_dict['PAYMENTMODE']
			order_object.txn_currency = response_dict['CURRENCY']
			order_object.save() 
			subscription_status = True
			profile_views.add_fields_to_profile(user, subscription_status,order_object.txn_date)            
			print("payment success")
			return render(request, 'orderStatus.html', {'response_dict':response_dict})
		else:
			order_object.payment_successful = False
			order_object.save()
			print("payment failed")
			return render(request, 'orderStatus.html', {'response_dict':response_dict})

	print("unsuccessfull")
	return render(request, 'orderStatus.html', {'response_dict':response_dict})
			
