from django.contrib import admin
from .models import WithdrawalMethod, WithdrawalType
# Register your models here.

admin.site.register(WithdrawalMethod)
admin.site.register(WithdrawalType)