from django.db import models

class SignInBonus(models.Model):
    voucher_name = models.CharField(max_length=150,blank=True,null=True)
    voucher_code = models.CharField(max_length=150)
    limit_voucher_usage = models.CharField(max_length=150, null=True)
    voucher_discount = models.CharField(max_length=150)
    maximum_discount = models.CharField(max_length=150 ,blank=True,null=True )
    voucher_description = models.TextField()

    def __str__(self):
        return str(self.voucher_code)

class SignInBonusUsage(models.Model):
    amount=models.CharField(max_length=150, blank=True, null=True)
    coupen_code = models.CharField(max_length=150)
    user_uuid = models.CharField(max_length=150)
    voucher_discount = models.CharField(max_length=150)
    status = models.BooleanField(default=True )
    dateTime= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.voucher_code)