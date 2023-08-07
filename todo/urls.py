"""
URL configuration for todo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.signin ,name='signin'),
    path('home/', views.home , name='home'),
    path('home/create/', views.create, name='create'),
    path('home/show/', views.show, name='show'),
    path('home/update/', views.update, name='update'),
    path('home/delete/', views.deletedata, name='deletedata'),
    path('home/deleteid/<int:id>/', views.deleteid, name='deleteid'),
    path('home/update/<int:id>/', views.updatedetails, name='updatedetails'),
    path('logout/',views.user_logout, name ='userlogout'),
    path('signup',views.sign_up, name='sign_up'),
]
