from django.contrib import admin

# Register your models here.
from kazakhapp.models import *

admin.site.register(City)
admin.site.register(Comment)
admin.site.register(User)
admin.site.register(Artist)
admin.site.register(Region)