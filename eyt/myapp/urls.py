from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('counter', views.counter, name='counter'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('post/<str:pk>', views.post, name='post'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('training_materials', views.training_materials, name='training_materials'),
    path('index.html', views.contact, name='contact'),
    path('home', views.home, name='home.html'),
    path('room', views.room, name='room.html'),
    path('all', views.all, name='all.html'),
    path('mentorship/', views.mentorship_application, name='mentorship_application'),
    path('upload_video/', views.upload_video, name='upload_video'),
    path('send-info/', views.send_info, name='send_info')
]


    