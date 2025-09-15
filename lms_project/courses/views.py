from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, CourseForm, LessonForm
from .models import Course

# ثبت‌نام کاربر
def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'courses/signup.html', {'form': form})


# صفحه اصلی - لیست دوره‌ها
@login_required
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})


# اضافه کردن دوره (فقط استاد)
@login_required
def add_course(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.teacher = request.user
            course.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'courses/add_course.html', {'form': form})


# جزئیات دوره + جلسات
@login_required
def course_detail(request, pk):
    course = Course.objects.get(pk=pk)
    lessons = course.lessons.all()
    return render(request, 'courses/course_detail.html', {'course': course, 'lessons': lessons})


# اضافه کردن جلسه
@login_required
def add_lesson(request, pk):
    course = Course.objects.get(pk=pk)
    if request.method == "POST":
        form = LessonForm(request.POST, request.FILES)
        if form.is_valid():
            lesson = form.save(commit=False)
            lesson.course = course
            lesson.save()
            return redirect('course_detail', pk=pk)
    else:
        form = LessonForm()
    return render(request, 'courses/add_lesson.html', {'form': form, 'course': course})
