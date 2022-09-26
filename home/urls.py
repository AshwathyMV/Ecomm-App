from django.urls import path
from home import views

#functionbased
# urlpatterns=[
#     path("home",views.index),
#     path("login",views.login),
#     path("registration",views.registration)
# ]

#class based

urlpatterns=[
    path("index",views.IndexView.as_view()),
    path("register",views.RegistrationView.as_view()),
    path("login",views.LoginView.as_view())
]
