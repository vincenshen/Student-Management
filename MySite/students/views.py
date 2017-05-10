from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login, logout, authenticate

from .models import Students
# Create your views here.


class StudentView(View):
    def get(self, request):
        students = Students.objects.all()
        return render(request, "index.html", {"students": students})


class LoginView(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        user_name = request.POST.get("username", "")
        pass_word = request.POST.get("password", "")
        user = authenticate(username=user_name, password=pass_word)
        if user:
            login(request, user)
            return redirect(reverse("students:student"))
        else:
            return render(request, "login.html", {"msg": "Incorrect username or password!"})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse("students:student"))


class RegisterView(View):
    def get(self, request):
        return render(request, "register.html")

    def post(self, request):
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        password2 = request.POST.get("password2", "")
        if password == password2:
            User.objects.create(username=username, password=make_password(password))
            return render(request, "register_success.html")
        else:
            return render(request, "register.html", {"msg": "username or password non-compliance!"})


class StudentAddView(View):
    def post(self, request):
        student = Students()
        student.name = request.POST.get("name", "")
        student.age = request.POST.get("age", "")
        student.grade = request.POST.get("grade", "")
        student.course = request.POST.get("course", "")
        student.enroll_date = request.POST.get("enroll_date", "")
        student.save()
        return redirect(reverse("students:student"))


class StudentDelView(View):
    def post(self, request):
        s_id = int(request.POST.get("s-d-id", ""))
        Students.objects.filter(id=s_id).delete()
        return redirect(reverse("students:student"))


class StudentUpdateView(View):
    def post(self, request):
        s_id = request.POST.get("s-id", "")
        s_name = request.POST.get("s-name", "")
        s_age = request.POST.get("s-age", "")
        s_grade = request.POST.get("s-grade", "")
        s_course = request.POST.get("s-course", "")
        s_date = request.POST.get("s-date", "")
        Students.objects.filter(id=s_id).update(name=s_name, age=s_age, grade=s_grade, course=s_course, enroll_date=s_date)
        return redirect(reverse("students:student"))