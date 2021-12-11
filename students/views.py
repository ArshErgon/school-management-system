from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

import datetime

from schoolUsers.models import UserRegistion

from .models import Student


# Create your views here.

def homeView(request):
    username = request.user.username
    all_student = len(Student.objects.all())
    school_user = UserRegistion.objects.filter(username=username)
    for i in school_user:
        pass
    print(i.insitution)
    school_students = Student.objects.filter(insitution=i.insitution)
    students_12 = school_students.filter(student_present_class='12')
    students_11 = school_students.filter(student_present_class='11')
    students_10 = school_students.filter(student_present_class='10')
    students_9 = school_students.filter(student_present_class='9')
    students_8 = school_students.filter(student_present_class='8')
    students_7 = school_students.filter(student_present_class='7')
    students_6 = school_students.filter(student_present_class='6')
    students_5 = school_students.filter(student_present_class='5')
    students_4 = school_students.filter(student_present_class='4')
    students_3 = school_students.filter(student_present_class='3')
    students_2 = school_students.filter(student_present_class='2')
    students_1 = school_students.filter(student_present_class='1')
    students_lkg = school_students.filter(student_present_class='LKG')
    students_ukg = school_students.filter(student_present_class='UKG')
    students_nusery = school_students.filter(student_present_class='NUSERY')
    print(students_ukg)

    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('students:visitor'))
     
    return render(request, 'index.html', {'student_information':Student.objects.all(), 'i':i, 'all_student':all_student, 'school_user':school_user
    ,'students_12':students_12, 
    'students_11':students_11, 
    'students_10':students_10, 
    'students_9':students_9 ,
    'students_8':students_8, 
    'students_7':students_7,
    'students_6':students_6,
    'students_5':students_5,
    'students_4':students_4,
    'students_3':students_3,
    'students_2':students_2,
    'students_1':students_1,
    'students_lkg':students_lkg,
    'students_ukg':students_ukg,
    'students_nusery':students_nusery,
    })


def all_student_display(request):
    username = request.user.username
    all_student = len(Student.objects.all())
    school = UserRegistion.objects.filter(username=username)
    for i in school:
        pass
    return render(request, 'student/all_student.html', {'student_information':Student.objects.all(), 'i':i, 'all_student':all_student})



def notAuthenticUser(request):
    return render(request, 'display.html')

# Add slug here
def detailsView(request, pk):
    # print(dir(request)) 
    dateInfo = str(datetime.datetime.today().day) + '/' + str(datetime.datetime.today().month) + '/' + str(datetime.datetime.today().year)
    for i in Student.objects.filter(pk=pk):
        pass

    return render(request, 'student/details.html', {'dateInfo':dateInfo, 'student':i})


# redirect to the request again.
def deleteStudent(request, pk):
    Student.objects.filter(pk=pk).delete()
    return render(request, 'index.html', {'student_information':Student.objects.all()})


def editStudent(request, pk):
    for showing_student_to_edit in Student.objects.filter(pk=pk):
        pass
    if request.method == 'POST':
        post_edit = Student.objects.get(id=pk)
        add_info = request.POST.get
        post_edit.fName = add_info("fname")
        post_edit.sName = add_info("sname")
        post_edit.student_code = add_info("sCode")
        post_edit.FatherName = add_info("fatherName")
        post_edit.MotherName = add_info("motherName")
        post_edit.fee = add_info("fee")
        post_edit.DOB = add_info("dob")
        post_edit.presentClass = add_info("presentClass")
        post_edit.address = add_info("address")
        post_edit.state = add_info("state")
        post_edit.city = add_info("city")
        post_edit.phoneNumber = add_info("phone_number")
        post_edit.adhaar = add_info("adhaar")
        post_edit.religion = add_info("religion")
        post_edit.caste = add_info("caste")
        post_edit.category = add_info("category")
        post_edit.rte_student = add_info("rte")
        post_edit.relatives_in_school = add_info("relatives")
        post_edit.email = add_info("emailfield")
        if post_edit.rte_student == "on":
            rte_ = True
        else:
            rte_ = False
        post_edit.rte_student = rte_
        post_edit.save()
        return redirect('/')
    return render(request, 'student/edit.html', {'student':showing_student_to_edit})


def addStudent(request):
    username = request.user.username
    school = UserRegistion.objects.filter(username=username)
    for i in school:
        pass

    if request.method == 'POST':
        add_info = request.POST.get
        insitution = i.insitution
        fName = add_info("fname")
        sName = add_info("sname")
        student_code = add_info("sCode")
        FatherName = add_info("fatherName")
        MotherName = add_info("motherName")
        fee = add_info("fee")
        DOB = add_info("dob")
        presentClass = add_info("presentClass")
        address = add_info("address")
        state = add_info("state")
        city = add_info("city")
        phoneNumber = add_info("phone_number")
        adhaar = add_info("adhaar")
        religion = add_info("religion")
        caste = add_info("caste")
        category = add_info("category")
        rte_student = add_info("rte")
        relatives_in_school = add_info("relatives")
        email = add_info("emailfield")
        if rte_student == "on":
            rte_ = True
        else:
            rte_ = False
        Student.objects.create(insitution=insitution, student_code=student_code, fName = fName, sName = sName, fatherName = FatherName, motherName = MotherName, fee = fee, DOB = DOB,  student_present_class=presentClass, address = address, phoneNumber = phoneNumber, email=email, adhaar= adhaar, religion=religion, caste=caste, category=category, rte_student=rte_, relatives_in_school=relatives_in_school, state=str(state).replace('_', ' '), city=city)
        return redirect('students:index')        
    return render(request, 'student/addingstudent.html', {'i':i})