from django.contrib import admin

# Register your models here.
from .models import SignInBonus
from .models import SignInBonusUsage
admin.site.register(SignInBonus)
admin.site.register(SignInBonusUsage)