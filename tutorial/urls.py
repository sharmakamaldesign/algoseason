from django.urls import path
from . import views

app_name = 'tutorial'

urlpatterns = [
    path('syllabus',views.Tutorial.getSyllabusCategoryAndSubCategory,name='getSyllabusCategoryAndSubCategory'),
    path('syllabus/<slug:subCategorySlug>',views.Tutorial.getContentBySubCategory,name='getContentBySubCategory'),
    path('syllabus/<slug:subCategorySlug>/<slug:contentSlug>',views.Tutorial.getContentByContentSlug,name='getContentByContentSlug'),
    


]