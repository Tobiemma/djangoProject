from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from uni.models import *
from uni.form import *

# Create your views here.


def get_veranstaltung_list(request):
    lessons = Lehrveranstaltung.objects.all().order_by('title')
    return render(request, 'uni/veranstaltung_list.html', {'page_title': 'Meine Lehrveranstaltungen',
                                                           'lessons': lessons})


def get_student_list(request):
    students = Studierende.objects.all().order_by('lastN', 'firstN')

    return render(request, 'uni/student_list.html', {'page_title': 'Studierenden',
                                                     'students': students, })


def add_student(request, pk=None):
     if pk:
        student = Studierende.objects.get(pk=pk)
     else:
         student = Studierende()

     if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student saved')
            return HttpResponseRedirect(reverse_lazy('student_list'))
        else:
            messages.error(request, 'Data incorrect')

     else:
        form = StudentForm(instance=student)

     return render(request, 'uni/add_student.html', {'page_title': 'Studierende hinzufügen', 'form': form, })
