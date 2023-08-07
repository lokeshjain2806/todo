from django.contrib import admin
from .models import Usermodel

# Register your models here.


@admin.register(Usermodel)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'Name', 'Fathers_Name', 'Email_Id', 'Contact_No', 'Address')
