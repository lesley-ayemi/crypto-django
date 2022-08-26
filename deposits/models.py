import os
from django.utils.translation import gettext as _
from django.db import models
from accounts.models import CustomUser

# Create your models here.
def get_deposit_upload_path(dirname, obj, filename):
    return os.path.join("deposits", dirname, obj.CustomUser.email, filename)

class DepositMethod(models.Model):
    ACTIVE = 'active'
    INACTIVE = 'inactive'
    STATUS = [
        (ACTIVE, _('Active')),
        (INACTIVE, _('Inactive')),
    ]
    deposit_name = models.CharField(max_length=50)
    deposit_address = models.CharField(max_length=255)
    deposit_status = models.CharField(max_length=50, choices=STATUS, default=ACTIVE)
    deposit_upload = models.FileField(blank=True, upload_to=get_deposit_upload_path, null=True)
    
    class Meta:
        verbose_name_plural = 'Deposit Method'
        
    def __str__(self):
        return self.deposit_name
    
    

class UserDeposit(models.Model):
    APPROVED = 'approved'
    PENDING = 'pending'
    DECLINED = 'declined'
    DEPOSIT_STATUS = [
        (APPROVED, _('approved')),
        (PENDING, _('pending')),
        (DECLINED, _('declined')),
    ]
    user_deposit = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    user_deposit_type = models.ForeignKey(DepositMethod, models.CASCADE, related_name='deposits')
    user_deposit_amount = models.PositiveSmallIntegerField()
    user_deposit_upload = models.FileField(upload_to=get_deposit_upload_path, null=True)
    user_deposit_status = models.CharField(max_length=100, choices=DEPOSIT_STATUS, default=PENDING)
    
    class Meta:
        verbose_name_plural = 'User Deposits'
    
    def __str__(self):
        return self.user_deposit
    