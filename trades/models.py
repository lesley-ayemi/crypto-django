from django.db import models
from accounts.models import CustomUser
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
)

# Create your models here.
class TradeCurrency(models.Model):
    currency_name = models.CharField(max_length=100, help_text='add currency')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.currency_name
    
    class Meta:
        verbose_name_plural = 'Add Currency'

class Trades(models.Model):
    order_id = models.IntegerField(unique=True, editable=False)
    user_trade = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    trade_date = models.DateField(auto_now_add=True)
    trade_time = models.TimeField(auto_now_add=True)
    currency_type = models.ForeignKey(TradeCurrency, on_delete=models.CASCADE, related_name='currencies', null=True, blank=True)
    trade_amount = models.DecimalField(
        validators=[MinValueValidator(0), MaxValueValidator(1000000000)],
        default=0,
        decimal_places=5,
        max_digits=100,
    )
    
    USER_TRADE_TYPE = (
        ('BY', 'BUY'),
        ('SL',  'SELL'),
    ) 
    trade_type = models.CharField(choices=USER_TRADE_TYPE, max_length=5)
    profit_loss = models.DecimalField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        blank=True,
        decimal_places=2,
        max_digits=12,
    )
    
    USER_TRADE_STATUS = [
        (1, 'ACTIVE'),
        (0, 'INACTIVE'),
    ]
    trade_status = models.CharField(choices=USER_TRADE_STATUS, max_length=10, default='ACTIVE')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # test_at = models.FileField(null=True, blank=True)
    
    def __str__(self):
        name = self.user_trade
        return f'{name} trade'
    
    class Meta:
        verbose_name_plural = 'Trade'