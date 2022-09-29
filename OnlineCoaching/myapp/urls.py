from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.show,name='show'),
    path('institute/',views.institute,name='institute'),
    path('admin_part/',views.admin_part,name='admin_part'),
    path('profile/',views.profile.as_view(),name='profile'),
    path('view_page/',views.View.as_view(),name='view_page'),
    path('update/<int:pk>',views.Update.as_view(),name='update'),
    path('delete/<int:pk>',views.Delete.as_view(),name='delete'),
    path('student_register/',views.register,name='student_register'),
    path('save_stu/',views.save_stu,name='save_stu'),
    path('student_login/',views.student_login,name='student_login'),
    path('validate/',views.validate,name='validate'),
    path('courses/',views.courses,name='courses'),
    path('click/',views.click,name='click'),
]
