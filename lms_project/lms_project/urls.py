from django.contrib import admin
from django.urls import path
from courses.views import signup_view, course_list, add_course, course_detail, add_lesson
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('signup/', signup_view, name='signup'),
    path('', course_list, name='course_list'),
    path('courses/add/', add_course, name='add_course'),
    path('courses/<int:pk>/', course_detail, name='course_detail'),
    path('courses/<int:pk>/add_lesson/', add_lesson, name='add_lesson'),
    
    # مسیر لاگین و لاگ‌اوت
    path('login/', auth_views.LoginView.as_view(template_name='courses/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    # اضافه کردن مسیر پیش‌فرض جنگو (اختیاری)
    path('accounts/login/', auth_views.LoginView.as_view(template_name='courses/login.html'), name='accounts_login'),
]

