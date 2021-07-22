from django.db import models
from django.urls import reverse


class SyllabusCategory(models.Model):
    name = models.CharField(max_length=250, unique=True)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(max_length=250, unique=True)
    index = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'syllabus_category'
        ordering = ('index',)
        verbose_name = 'syllabus_category'
        verbose_name_plural = 'syllabus_categories'

    def __str__(self):
        return '{}'.format(self.name)

class SyllabusSubCategory(models.Model):
    name = models.CharField(max_length=250, unique=True)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(max_length=250, unique=True)
    index = models.IntegerField(null=True, blank=True)
    category = models.ForeignKey(SyllabusCategory, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.name)
    def get_url(self):
        return reverse('tutorial:getContentBySubCategory', args=[self.slug])

class SyllabusType(models.Model):
    name = models.CharField(max_length=250,unique=True)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(max_length=250, unique=True)

    class Meta:
        db_table = 'syllabus_type'
        ordering = ('name',)
        verbose_name = 'syllabus_type'
        verbose_name_plural = 'syllabus_types'

    def __str__(self):
        return '{}'.format(self.name)

class Syllabus(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    index = models.IntegerField(null=True, blank=True)
    description = models.TextField(blank=True)
    category = models.ForeignKey(SyllabusCategory, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(SyllabusSubCategory, on_delete=models.CASCADE)
    video_file = models.FileField(upload_to='syllabus_video',null=True, blank=True)
    text_content_file = models.FileField(upload_to='syllabus_file', null=True, blank=True)
    syllabus_type = models.ForeignKey(SyllabusType, on_delete=models.CASCADE)


    class Meta:
        db_table = 'syllabus'
        ordering = ('category',)
        verbose_name = 'syllabus'
        verbose_name_plural = 'syllabus'

    def __str__(self):
        return '{}'.format(self.name)

    def get_url(self,subCategorySlug):
        return reverse('tutorial:syllabusContent', args=[subCategorySlug.slug,self.slug])




