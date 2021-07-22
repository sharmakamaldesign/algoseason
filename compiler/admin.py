from django.contrib import admin
from .models import UserCode, TestInput, TestOutput

class UserCodeAdmin(admin.ModelAdmin):
    list_display = ['createdAt','code_file','syllabus']

class TestInputAdmin(admin.ModelAdmin):
    list_display = ['file','syllabus','time_limit']

class TestOutputAdmin(admin.ModelAdmin):
    list_display = ['file','syllabus','time_limit']

admin.site.register(UserCode, UserCodeAdmin)
admin.site.register(TestInput, TestInputAdmin)
admin.site.register(TestOutput, TestOutputAdmin)

