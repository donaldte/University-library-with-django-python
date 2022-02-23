
from django.contrib import admin
from .models import User, Ebooks, Books, Ecategory, Profile, Chats, SendFeedback, CommandBook

# Register your models here.

class AdminProfile(admin.ModelAdmin):
    list_display  = ('user', 'matricule', 'school', 'department' )


class AdminBook(admin.ModelAdmin):    
    list_display = ('title', 'author', 'category', 'date_added')


class AdmineBook(admin.ModelAdmin):    
    list_display = ('title', 'author', 'category', 'date_added')  

class AdminChat(admin.ModelAdmin):
    list_display = ('user', 'message', 'posted_at')  

class AdminCommand(admin.ModelAdmin):
    list_display = ('student_name', 'comand_date',  'confirm')     


admin.site.register(User)
admin.site.register(Ebooks, AdmineBook)
admin.site.register(Books, AdminBook)
admin.site.register(Ecategory)
admin.site.register(Profile, AdminProfile)
admin.site.register(Chats, AdminChat)
admin.site.register(SendFeedback)
admin.site.register(CommandBook, AdminCommand)
