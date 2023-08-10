from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from conf.forms import StudentRegistration, Signupform
from conf.models import Usermodel
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from braces.views import PermissionRequiredMixin,LoginRequiredMixin


# Create your views here.

def get(request):
    form = Signupform()
    return render(request, 'sign_up.html', {'form': form})


class SignUp(View):
    def post(self,request):
        form = Signupform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')
        else:
            return HttpResponse("<h1>Something Went Wrong With Details</h1>")



class Home(View):
        def get(self,request):
                return render(request,'base.html')


class Create(View):
    def get(self,request):
            form= StudentRegistration()
            context = {"form" : form}
            return render(request,'create.html' , context)

    def post(self , request):
            form = StudentRegistration(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home')


class Show(View):
    def get(self, request):
        retrieve_data = Usermodel.objects.all()
        return render(request, 'read.html', {"retrieve_data": retrieve_data})


class Update(LoginRequiredMixin,PermissionRequiredMixin,View):
    permission_required= 'conf.can_view_email_id'
    def get(self,request):
            retrieve_data = Usermodel.objects.all()
            return render(request, 'update.html', {"retrieve_data": retrieve_data})


class UpdateDetails(View):
    def get(self,request,id):
        data = Usermodel.objects.get(pk=id)
        form = StudentRegistration(instance=data)
        return render(request, 'updatedetails.html' , {'form':form , 'id':id})

    def post(self,request,id):
        data =Usermodel.objects.get(pk=id)
        form = StudentRegistration(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('home')

class DeleteDataView(View):
    def get(self,request):
        retrieve_data = Usermodel.objects.all()
        return render(request, 'delete.html', {"retrieve_data": retrieve_data})


class DeleteDetails(View):
    def get(self,request,id):
        retrieve_data = Usermodel.objects.get(pk=id).delete()
        context = {"retrieve_data": retrieve_data}
        return redirect('deletedata')


class UserLogout(View):
    def get(self,request):
        logout(request)
        return redirect('signin')

class SignIn(View):
    def get(self,request):
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

    def post(self,request):
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            users = authenticate(username=username, password=password)
            if users is not None:
                login(request,users)
                return redirect('home')
        else:
            return HttpResponse("Please Enter Valid Details")


########################################
# def signin(request):
#     if not request.user.is_authenticated:
#         if request.method == 'POST':
#             form = AuthenticationForm(request=request,data=request.POST)
#             if form.is_valid():
#                 username = form.cleaned_data['username']
#                 password = form.cleaned_data['password']
#                 users = authenticate(username=username, password=password)
#                 if users is not None:
#                     login(request,users)
#                     return redirect('home')
#         else:
#             form = AuthenticationForm()
#         return render(request,'login.html',{'form': form})
#     else:
#         return redirect('home')

# def user_logout(request):
#     logout(request)
#     return redirect('signin')


# def sign_up(request):
#     if request.method == 'POST':
#         form = Signupform(request.POST)
#         if form.is_valid():
#             form.save()
#     else:
#         form = Signupform()
#     return render(request, 'sign_up.html' , {'form': form})


#Function Based View

# def home(request):
#     if request.user.is_authenticated:
#         return render(request, 'base.html')
#     else:
#         return redirect('signin')


# def create(request):
#     if request.user.is_authenticated:
#         if request.method == 'POST':
#             form = StudentRegistration(request.POST)
#             if form.is_valid():
#                 form.save()
#                 return redirect('home')
#         else:
#             form = StudentRegistration()
#         return render(request, 'create.html', {"form": form})
#     else:
#         return redirect('signin')


# def show(request):
#     if request.user.is_authenticated:
#         retrieve_data = Usermodel.objects.all()
#         return render(request, 'read.html',{"retrieve retrieve_data= User.obects.all()
#         return render(request, 'read.html', {"retrieve_data": retrieve_data})_data": retrieve_data})
#     else:
#         return redirect('signin')


# def update(request):
#     if request.user.is_authenticated:
#         retrieve_data = Usermodel.objects.all()
#         return render(request, 'update.html', {"retrieve_data": retrieve_data})
#     else:
#         return redirect('signin')


# def deletedata(request):
#     if request.user.is_authenticated:
#         retrieve_data = Usermodel.objects.all()
#         return render(request, 'delete.html', {"retrieve_data": retrieve_data})
#     else:
#         return redirect('signin')


# def updatedetails(request, id):
#     if request.user.is_authenticated:
#         if request.method == 'POST':
#             data = Usermodel.objects.get(pk=id)
#             form = StudentRegistration(request.POST, instance=data)
#             if form.is_valid():
#                 form.save()
#                 return redirect('home')
#         else:
#             data = Usermodel.objects.get(pk=id)
#             form = StudentRegistration(instance=data)
#         return render(request, 'updatedetails.html', {'form': form})
#     else:
#         return redirect('signin')


# def deleteid(request,id):
#     if request.user.is_authenticated:
#         retrieve_data = Usermodel.objects.get(pk=id)
#         retrieve_data.delete()
#         context = {"retrieve_data": retrieve_data}
#         return redirect('deletedata')
#     else:
#         return redirect('signin')

