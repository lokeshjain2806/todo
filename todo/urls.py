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
    path('', views.SignIn.as_view() ,name='signin'),
    path('signup',views.SignUp.as_view(), name='sign_up'),
    path('home/', views.Home.as_view() , name='home'),
    path('home/create/', views.Create.as_view(), name='create'),
    path('home/show/', views.Show.as_view(), name='show'),
    path('home/update/', views.Update.as_view(), name='update'),
    path('home/update/<int:id>/', views.UpdateDetails.as_view(), name='updatedetails'),
    path('home/delete/', views.DeleteDataView.as_view(), name='deletedata'),
    path('home/deleteid/<int:id>/', views.DeleteDetails.as_view(), name='deleteid'),
    path('logout/',views.UserLogout.as_view(), name ='userlogout'),

]
