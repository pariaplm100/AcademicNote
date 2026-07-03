from django.contrib import admin
from notes.models import user

# Register your models here.

class userAdmin(admin.ModelAdmin): 
    date_heirarchy="create_time"
    
