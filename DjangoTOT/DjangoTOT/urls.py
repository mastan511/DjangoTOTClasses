"""DjangoTOT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from djtot import views
from djbt import views as v
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home),
    path('ft/',views.fun),
    path('rcd/<str:name>',views.rc),
    path('table/<int:n>',views.mulTable),
    path('details/<str:name>/<int:age>',views.myDetails),
   	path('de/',views.sample),
   	path('js/',views.myJs),
   	path('login/',views.mylogin),
   	path('reg/',views.myreg),
   	path('arthematic/',views.myarthematic),
    path('',v.home),
    path('task/',v.bttask),
    path('registration/',v.regtask),
    path('regd/',v.regd),
    path('DB/',include('DB.urls')),

]
