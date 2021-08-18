from django.contrib import admin

# Register your models here.
from .models import Betta, Feeding

admin.site.register(Betta)
admin.site.register(Feeding)