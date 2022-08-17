from django.urls import path
from .import views

urlpatterns = [
    path("",views.index,name="index"),
    path("joinus",views.joinus,name="joinus"),
    path("home",views.home,name="home"),
    path("signup",views.signup,name="signup"),
    path('signout/',views.signout, name='signout'),
    path('signin/',views.signin, name='signin'),
    path('profile/',views.profile, name='profile'),

    path('about',views.about, name='about'),
    path('blog',views.blog, name='blog'),
    path('contact',views.contact, name='contact'),
    path('services',views.services, name='services'),
   
]