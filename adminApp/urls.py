from . import views
from django.urls import path

urlpatterns = [
    path('hello',views.hello,name="hello"),
    path('',views.admin_home,name="adminhome")

]
