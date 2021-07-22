from django.contrib import admin
from .models import SyllabusCategory, Syllabus, SyllabusSubCategory,SyllabusType


class SyllabusCategoryAdmin(admin.ModelAdmin):
    list_display = ['name','index','slug']
    prepopulated_fields = {'slug': ('name',)}

class SyllabusSubCategoryAdmin(admin.ModelAdmin):
    list_display = ['name','index','slug','category']
    prepopulated_fields = {'slug': ('name',)}


class SyllabusAdmin(admin.ModelAdmin):
    list_display = ['name', 'index', 'description',
                    'category', 'sub_category', 'video_file', 'text_content_file','syllabus_type']
    prepopulated_fields = {'slug': ('name',)}

class SyllabusTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'description',]
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(SyllabusCategory, SyllabusCategoryAdmin)
admin.site.register(SyllabusSubCategory, SyllabusSubCategoryAdmin)
admin.site.register(Syllabus, SyllabusAdmin)
admin.site.register(SyllabusType, SyllabusTypeAdmin)

