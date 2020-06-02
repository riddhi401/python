from django.shortcuts import render,redirect
from .forms import StudentForm
from . models import student



def student_list(request):
    context = {
        'student_list':student.objects.all()
    }
    return render(request,'student_list.html',context)


def student_form(request,id=0):
    if request.method == "GET":
        if id == 0:
            form = StudentForm()
        else:
            students = student.objects.get(pk=id)
            form = StudentForm(instance=students)
        return render(request,'student_form.html',{'form':form})

    else:
        if id == 0:
            form = StudentForm(request.POST)
        else:
            students = student.objects.get(pk=id)
            form = StudentForm(request.POST,instance=students)
        if form.is_valid():
            form.save()
            return redirect('/student/list')



def student_delete(request,id):
    students = student.objects.get(pk=id)
    students.delete()
    return redirect('/student/list')





    


