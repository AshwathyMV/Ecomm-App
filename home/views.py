from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
# Create your views here.

#function based & class based views
#classbased is better

#function based view
# def index(request):
#     # return HttpResponse("<h1>Hello World</h1>")
#       return render(request,"home.html")
# def login(request):
#     # print(request.method)
#     # return HttpResponse("<h1>Click Below to login</h1>")
#     return render(request,"login.html")
# def registration(request):
#     # return HttpResponse("<h1>Registration</h1>")
#       return render(request,"registration.html")

#class based view

#import --> from django.views.generic import View <--- this is View is the parent class

class IndexView(View):

    def get(self,request):
        return render(request,"home.html")

class RegistrationView(View):

    def get(self,request):
        return render(request24,"registration.html")
    def post(self,request):
        # print("here in post")
        # print(request.method)
        # print(request)
        # print(request.POST)
        print(request.POST["f_name"])
        print(request.POST["l_name"])
        print(request.POST["e_mail"])
        # print(request.POST["u_name"])
        # print(request.POST["pwd"])
        print(request.POST.get("pwd"))
        print(request.POST.get("u_name"))
        return render(request, "registration.html")

class LoginView(View):

    def get(self,request):
        return render(request,"login.html")
    def post(self,request):
        print(request.POST.get("u_name"))
        print(request.POST.get("pwd"))
        return render(request, "login.html")

