from django.shortcuts import render
import datetime
from datetime import date
from .models import UserProfile
# Create your views here.
COURSE_VALIDITY_IN_YEAR = 1
def addYears(date_time_string, add_years):
    # date_time_str = date_time
    date_time_obj = datetime.datetime.strptime(date_time_string, '%Y-%m-%d %H:%M:%S.%f')
    try:
       return date_time_obj.replace(year = date_time_obj.year + add_years)
    except ValueError:
    #If not same day, it will return other, i.e.  February 29 to March 1 etc.
        return date_time_obj + (date(date_time_obj.year + add_years, 1, 1) - date(date_time_obj.year, 1, 1))


def add_fields_to_profile(user,is_subscribed, subscription_date):
    
    subscription_expiry_date = addYears(subscription_date,COURSE_VALIDITY_IN_YEAR)
    user_profile_object = UserProfile.objects.get(user = user)
    user_profile_object.is_subscribed = is_subscribed
    user_profile_object.subscription_date = subscription_date
    user_profile_object.subscription_expiry_date = subscription_expiry_date
    user_profile_object.save()

def user_profile(request):
    return render(request,'user_profile.html')