from algoseason.settings import BASE_DIR
from django.contrib.auth.models import User
from tutorial.models import Syllabus
from django.shortcuts import render
from django.http import JsonResponse
import subprocess
from .models import UserCode, TestInput, TestOutput
import os
import filecmp
# Create your views here.


def compileCppCode(request):

    print('hello world')
    cSyllabus = Syllabus.objects.get(id=request.POST.get('syllabus'))
    file = request.FILES.get('file')
    userCode = UserCode.objects.create(
        is_correct_answer=False,
        code_file=file,
        syllabus=cSyllabus,
        user=request.user,
        status='pending',)
    try:
        codePath = str("static/media/"+str(userCode.code_file))
        file_name_without_extension = codePath.split('/')[-1].split('.')[0]
        comopileProgram = subprocess.Popen('g++ -o static/media/submitted_code_file/{0}/{1}/{2} {3}'.format(
            request.user.id, cSyllabus.id, file_name_without_extension, codePath), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        comopileProgram.wait()
        (stdout, stderr) = comopileProgram.communicate()

        if comopileProgram.returncode != 0:
            print(stderr)
            return JsonResponse({'data': str(stderr),'error':'Runtime Error'})

        testInputFiles = TestInput.objects.filter(syllabus_id=cSyllabus.id)
        testOutputFiles = TestOutput.objects.filter(syllabus_id=cSyllabus.id)
        results = {
            'status':1,
            'message': '',
            'testCaseResult': []

        }
        for i in range(0, len(testInputFiles)):
            print("loop", i)
            inputFilePath = 'static/media/{0}'.format(testInputFiles[i].file)
            outputFilePath = 'static/media/{0}'.format(testOutputFiles[i].file)
            programOutputFilePath = 'static/media/submitted_code_file/{0}/{1}/{2}'.format(
                request.user.id, cSyllabus.id, 'output'+str(i+1)+'.txt')

            runProgram = subprocess.Popen('./static/media/submitted_code_file/{0}/{1}/{2}<{3}>{4}'.format(
                request.user.id, cSyllabus.id, file_name_without_extension, inputFilePath, programOutputFilePath), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            runProgram.wait()
            (stdout, stderr) = comopileProgram.communicate()
            comp = filecmp.cmp(programOutputFilePath,
                               outputFilePath, shallow=False)
            print("Comp is ", comp)
            if comp==True:
                results['testCaseResult'].append("Correct Answer")
            else:
                results['status'] = 0
                results['testCaseResult'].append("Wrong Answer")


        print(results)
    except Exception as e:
        print("exception")
        print(e)
    else:
        print('run')

        # testInput = TestInput.objects.filter(Syllabus = cSyllabus)
        # testOutput = TestOutput.objects.filter(Syllabus = cSyllabus)
        # tmp=subprocess.call("./a.out<"+testInput+">codeOutput")

    # subprocess.call(["g++", "compiler/helloworld.cpp"])
    # # tmp = subprocess.check_output(["pwd"])
    # tmp=subprocess.check_output("./a.out")
    # print("printing result")
    # print(tmp)
    # print(request)
    return JsonResponse({
        'data': results
    })
