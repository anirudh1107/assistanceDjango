from django.contrib import admin
from .models import Shop,User,Item,Request,FinalBill


# Register your models here.
admin.site.register(Shop);
admin.site.register(User);
admin.site.register(Item);
admin.site.register(Request);
admin.site.register(FinalBill);
