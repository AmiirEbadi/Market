from django.contrib import admin
from .models import UserAccount, Address

# Register your models here.
@admin.register(UserAccount)
class UserAccountAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone_number', )
    

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('district', 'city', )
