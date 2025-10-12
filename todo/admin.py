from django.contrib import admin

# Register your models here.

from .models import Todo




class TodoAdmin(admin.ModelAdmin):
    #display list
    list_display = ('title', 'is_completed', 'created_at', 'updated_at')
    #search list
    search_fields = ('title',)

admin.site.register(Todo, TodoAdmin)
