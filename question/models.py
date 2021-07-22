from django.db import models
from django.urls import reverse
# Create your models here.
class QuestionCategory(models.Model):
	name = models.CharField(max_length= 250, unique=True)
	description = models.TextField(blank=True, null=True)

	class Meta:
		db_table='question_category'
		ordering = ('name',)
		verbose_name = 'question_category'
		verbose_name_plural = 'question_categories'
	def __str__(self):
	 	return '{}'.format(self.name)

class QuestoinDifficulty(models.Model):
	name = models.CharField(max_length= 250, unique=True)
	description = models.TextField(blank=True, null=True)

	class Meta:
		db_table='question_difficulty'
		ordering = ('name',)
		verbose_name = 'question_difficulty'
		verbose_name_plural = 'question_difficulties'
	def __str__(self):
	 	return '{}'.format(self.name)

class Question(models.Model):
	name = models.CharField(max_length= 250, unique=True)
	slug = models.SlugField(max_length=250, unique=True)
	description = models.TextField(blank=True)
	category = models.ForeignKey(QuestionCategory,on_delete=models.CASCADE)
	difficulty = models.ForeignKey(QuestoinDifficulty, on_delete=models.CASCADE)
	video_file = models.FileField(upload_to='question_video')
	question_file = models.FileField(upload_to='question_file')
	sample_input = models.TextField(blank=True)
	sample_output = models.TextField(blank=True)

	class Meta:
		db_table='question'
		ordering = ('name',)
		verbose_name = 'question'
		verbose_name_plural = 'questions'
	
	def __str__(self):
	 	return '{}'.format(self.name)

	def get_url(self):
		return reverse('question:question_detail',args=[self.slug])
