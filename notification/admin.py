from django.contrib import admin
from . models import Login, SendEmail

@admin.register(Login)
class LoginAdmin(admin.ModelAdmin):
    list_display = ['username','password']
    pass

@admin.register(SendEmail)
class SendEmailAdmin(admin.ModelAdmin):
    list_display = ['uuid','body','email','title','created','modified']
    pass

