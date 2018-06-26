from django.contrib import admin
from django.urls import path
from user_fun import views

urlpatterns = [
    path('login/',views.login ),
    path('loginout/',views.loginout ),
    path('useradd/',views.useradd ),
    path('useradmin/',views.useradmin),
    path('userdel/',views.userdel),
    # path('userupdate/',views.userupdate),
]
