from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class UserAccount(AbstractUser):
    phone_number = models.CharField(max_length=11, blank=False)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self) -> str:
        return self.username
    

class Address(models.Model):
    city = models.CharField(max_length=50, blank=False)
    district = models.CharField(max_length=50, blank=False)
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='addresses')

    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'
    
    def __str__(self) -> str:
        return self.city + " " + self.district
    