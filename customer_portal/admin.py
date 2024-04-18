from django.contrib import admin
from .models import Customer, Orders,Vehicles,CarDealer,Area

# Register your models here.
admin.site.register(Customer)
admin.site.register(Orders)
admin.site.register(Vehicles)
admin.site.register(CarDealer)
admin.site.register(Area)



