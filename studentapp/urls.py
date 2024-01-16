from django.urls import path
from studentapp import views

urlpatterns = [
    path('', views.login_fun, name='log'),
    path('regdata', views.regdata, name='reg'),
    path('insert', views.insert, name='insert'),
    path('display', views.display, name='display'),
    path('update/<int:id>', views.update, name='update'),
    path('del/<int:id>', views.delete_fun, name='del'),
    path('home', views.home_fun, name='home'),
    path('log_out', views.logout_fun, name='log_out'),
    path('forgetPassword', views.forgetPassword, name='forgetPassword'),
]