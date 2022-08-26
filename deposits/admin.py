from django.contrib import admin
from .models import DepositMethod, UserDeposit
# Register your models here.

admin.site.register(DepositMethod)
admin.site.register(UserDeposit)