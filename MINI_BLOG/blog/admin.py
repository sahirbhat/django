from django.contrib import admin
from .models import Post, Contact


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'desc']



@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','mobile','email','message']