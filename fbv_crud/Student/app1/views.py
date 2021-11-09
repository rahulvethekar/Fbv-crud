from django.shortcuts import redirect, render

from .forms import StudentForm
from .models import Student

# Create your views here.
def StudentFormView(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('studentData')

    
    context = {'form':form}
    template_name = 'app1/studentForm.html'
    return render(request,template_name,context)


def StudentDataView(request):
    obj = Student.objects.all()
    context = {'studentData':obj}
    template_name = 'app1/studentData.html'
    return render (request,template_name,context)


def StudentUpdateView(request,uid):
    obj = Student.objects.get(id=uid)
    form = StudentForm(instance=obj)
    if request.method == 'POST':
        form = StudentForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('studentData')
    context = {'form':form}
    temmplate_name = 'app1/studentForm.html'
    return render(request,temmplate_name,context)

def StudentDeleteView(request,did):
    obj = Student.objects.get(id=did)
    obj.delete()
    return redirect('studentData')






