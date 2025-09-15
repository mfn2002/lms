from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Course, Lesson

# فرم ثبت‌نام
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# فرم دوره
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description']


# فرم جلسه
class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['title', 'content', 'file']

