from django.contrib import admin

# Register your models here.
from bank_branches.models import Banks, Branches

admin.site.register(Banks)
admin.site.register(Branches)