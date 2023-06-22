from django.contrib import admin
from .models import Question , Answer
# Register your models here.

class ForumAdmin(admin.ModelAdmin):   # filter adminpanal
    list_display =['name' , 'date']
    list_filter = ['date' , 'name']
    
admin.site.register(Question,ForumAdmin)
admin.site.register(Answer)
