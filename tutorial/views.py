from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Syllabus, SyllabusCategory, SyllabusSubCategory
from django.contrib.auth.decorators import login_required

# Create your views here.
class Tutorial:
    currentSyllabus = None

    def setCurrentSyllabus(syllabus):
        currentSyllabus = Syllabus
    def getSyllabusCategoryAndSubCategory(request):
        syllabusCategories = SyllabusCategory.objects.all()
        syllabusSubCategories = SyllabusSubCategory.objects.all().order_by('index')
        # syllabus = Syllabus.objects.all()
        return render(request,'syllabus.html',{'syllabusCategories':syllabusCategories, 'syllabusSubCategories':syllabusSubCategories})

    @login_required(login_url='authentication:login')
    def getContentBySubCategory(request,subCategorySlug = None):
        print(request.user.user_profile)
        if request.user.user_profile.is_subscribed:
            subCategory = SyllabusSubCategory.objects.get(slug = subCategorySlug)
            allContents = Syllabus.objects.filter(sub_category = subCategory)
            print(allContents)
            return render(request,'syllabusContent.html',{'subCategory':subCategory,'allContents':allContents})

    @login_required(login_url='authentication:login')
    def getContentByContentSlug(request,subCategorySlug=None, contentSlug=None):
        if not request.user.user_profile.is_subscribed:
            return render(request,'order_details.html',{'course_price':399})
        subCategory = SyllabusSubCategory.objects.get(slug = subCategorySlug)
        allContents = Syllabus.objects.filter(sub_category = subCategory)
        print(allContents[0].syllabus_type_id) 
        selectedContent = None
        if contentSlug == '__all__':
            selectedContent = allContents[0]
        else:
            selectedContent = Syllabus.objects.get(slug = contentSlug)
        print(allContents.values())
        file_path = selectedContent.text_content_file
        textFileContent = None
        if file_path is not None and file_path != '':
            
            print('file path is ',file_path)
            f = open("static/media/"+str(file_path), 'r')
            textFileContent = f.read()
            f.close()
        return render(request,'syllabusContent.html',{'subCategory':subCategory,'allContents':allContents, 'selectedContent':selectedContent, 'textFileContent':textFileContent})
        
