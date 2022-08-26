from django.contrib import admin
from . models import Trades, TradeCurrency
# Register your models here.
admin.site.register(Trades)
admin.site.register(TradeCurrency)