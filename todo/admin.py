from django.contrib import admin

# Register your models here.

from .models import Todo


#display list

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_completed', 'created_at', 'updated_at')

admin.site.register(Todo, TodoAdmin)
