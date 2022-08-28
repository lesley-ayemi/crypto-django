from django.db import models
from django.utils.translation import gettext as _

from accounts.models import CustomUser

# Create your models here.
class WithdrawalType(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Add Widthrawal Type'
    
class WithdrawalMethod(models.Model):
    APPROVED = 'approved'
    PENDING = 'pending'
    DECLINED = 'declined'
    STATUS = [
        (APPROVED, _('approved')),
        (PENDING, _('pending')),
        (DECLINED, _('declined')),
    ]
    
    w_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_withdrawal')
    w_type = models.ForeignKey(WithdrawalType, on_delete=models.CASCADE, related_name='user_withdrawal_type')
    w_address = models.CharField(max_length=255)
    w_amount = models.PositiveIntegerField()
    w_status = models.CharField(max_length=100, choices=STATUS, default=PENDING)
    
    def __str__(self):
        return self.w_user
    
    class Meta:
        verbose_name_plural = 'Add Withdrawl Method'