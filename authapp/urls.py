from django.urls import path
from authapp import views

urlpatterns = [
  path('',views.Home,name="Home"),
  path('', views.gallery, name='gallery'),
  path('signup',views.signup,name="signup"),
  path('login',views.handlelogin,name="handlelogin"),
  path('logout',views.handleLogout,name="handlelogout"),
  path('contact',views.contact,name="contact"),
  path('enroll',views.enroll,name="enroll"),
  path('profile',views.profile,name="profile"),
  path('gallery',views.gallery,name="gallery"),
  path('upload', views.upload_photo, name='upload_photo'),


]