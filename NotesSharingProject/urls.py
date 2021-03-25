"""NotesSharingProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from notes import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('login/',views.userlogin,name="login"),
    path('login_admin/',views.login_admin,name="login_admin"),
    path('signup/',views.signup,name="signup"),
    path('logout/',views.Logout,name="logout"),
    path('profile/',views.profile,name="profile"),
    path('view_userse/',views.view_users,name="view_users"),
    path('delete_mynotes/<int:pid>',views.delete_mynotes,name="delete_mynotes"),
    path('delete_users/<int:pid>',views.delete_users,name="delete_users"),
    path('view_mynotes/',views.view_mynotes,name="view_mynotes"),
    path('pending_notes/',views.pending_notes,name="pending_notes"),
    path('accepted_notes/',views.accepted_notes,name="accepted_notes"),
    path('rejected_notes/',views.rejected_notes,name="rejected_notes"),
    path('all_notes/',views.all_notes,name="all_notes"),
    path('delete_notes/<int:pid>',views.delete_notes,name="delete_notes"),
    path('viewallnotes/',views.viewallnotes,name="viewallnotes"),

    path('assign_status/<int:pid>',views.assign_status,name="assign_status"),
    path('upload_notes/',views.upload_notes,name="upload_notes"),
    path('edit_profile/',views.edit_profile,name="edit_profile"),
    path('changepassword/',views.changepassword,name="changepassword"),
    path('admin_home/',views.admin_home,name="admin_home"),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
