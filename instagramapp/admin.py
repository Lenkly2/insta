from django.contrib import admin
from .models import CustomUser,Post,Coment,Massage
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Post)
admin.site.register(Coment)
admin.site.register(Massage)