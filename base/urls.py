from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('result',views.result,name="result"),
    path('appointment',views.appointment,name="appointment"),
    path('success',views.sendMail,name="success"),
]