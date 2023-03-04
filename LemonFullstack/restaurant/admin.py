from django.contrib import admin
from .models import Booking, MenuItem

# Register your models here.
from .models import Menu
from .models import Booking


admin.site.register(Menu)
admin.site.register(Booking)
admin.site.register(MenuItem)