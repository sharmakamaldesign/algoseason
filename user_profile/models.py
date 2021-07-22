from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class UserProfile(models.Model):
	first_name = models.CharField(max_length=250, null=True, blank=True)
	last_name = models.CharField(max_length=250, null=True, blank=True)
	is_subscribed = models.BooleanField(default=False)
	subscription_date = models.DateTimeField(blank=True, null=True)
	subscription_expiry_date = models.DateTimeField(blank=True, null=True)
	mobile_number = models.CharField(max_length=250, null=True, blank=True)
	# Address
	streen_address = models.CharField(max_length=250, null=True, blank=True)
	city = models.CharField(max_length=250, null=True, blank=True)
	pincode = models.CharField(max_length=250, null=True, blank=True)
	state = models.CharField(max_length=250, null=True, blank=True)
	country = models.CharField(max_length=250, null=True, blank=True)
	user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='user_profile')

	class Meta:
		db_table = 'UserProfile'
		# ordering = ['-created']

	def __str__(self):
		return str(self.id)

def create_user_profile(sender, instance, created, **kwargs):

    if created:

        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)
