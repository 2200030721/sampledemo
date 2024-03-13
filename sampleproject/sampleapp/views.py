from django.shortcuts import render
from .models import Student

def home(request):
    return render(request, 'home.html')

def addStudent(request):
    if request.method == 'POST':
        sname = request.POST['sname']
        course = request.POST['course']  # Fix the typo here
        fees = request.POST['fees']
        st = Student(sname=sname, course=course, fees=fees)
        st.save()
        return render(request, 'add_student.html', {'saved': True})
    return render(request, 'add_student.html')
