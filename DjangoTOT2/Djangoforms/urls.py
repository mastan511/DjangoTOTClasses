from django.urls import path
from Djangoforms import views
from .views import addEmployee

urlpatterns = [
path('addEmployee/',addEmployee),
path('dynamichtmlform/',views.dynamichtmlformgen,name = 'dhfg'),
# path('read/',read,name='read'),


]