from django.contrib import admin
from .models import QuestionCategory,Question, QuestoinDifficulty
# Register your models here.
class QuestionCategoryAdmin(admin.ModelAdmin):
	list_display = ['name',]
	# prepopulated_fields = {'slug':('name',)}

class QuestionDifficultyAdmin(admin.ModelAdmin):
	list_display = ['name',]
	# prepopulated_fields = {'slug':('name',)}

class QuestionAdmin(admin.ModelAdmin):
	list_display = ['name','description','category','difficulty','video_file','question_file']
	prepopulated_fields = {'slug':('name',)}

admin.site.register(QuestionCategory, QuestionCategoryAdmin)
admin.site.register(Question,QuestionAdmin)
admin.site.register(QuestoinDifficulty, QuestionDifficultyAdmin)