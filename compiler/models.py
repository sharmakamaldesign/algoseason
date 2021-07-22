from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
from tutorial.models import Syllabus
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
def getUploadPath(instance,fileName):
    print('instance is ', instance.syllabus.id)
    _datetime = datetime.now()
    datetime_str = _datetime.strftime("%Y-%m-%d-%H-%M-%S")
    return 'submitted_code_file/{0}/{1}/{2}-{3}'.format(instance.user.id,instance.syllabus.id,datetime_str,fileName)

def getTestInputFilePath(instance,fileName):
    return 'codeTestFiles/{0}/input/{1}'.format(instance.syllabus.slug,fileName)

def getTestOutputFilePath(instance,fileName):
    return 'codeTestFiles/{0}/output/{1}'.format(instance.syllabus.slug,fileName)
class UserCode(models.Model):
    createdAt = models.DateField(auto_now_add=True,)
    is_correct_answer = models.BooleanField(default=False)
    syllabus = ForeignKey(Syllabus, on_delete=CASCADE)
    user = ForeignKey(User,on_delete=CASCADE)
    code_file = models.FileField(upload_to=getUploadPath)
    status = models.CharField(max_length=250)


class TestInput(models.Model):
    file = models.FileField(upload_to=getTestInputFilePath)
    time_limit = models.IntegerField()
    syllabus = ForeignKey(Syllabus,on_delete=CASCADE)

class TestOutput(models.Model):
    file = models.FileField(upload_to=getTestOutputFilePath)
    time_limit = models.IntegerField()
    syllabus = ForeignKey(Syllabus,on_delete=CASCADE)

   
