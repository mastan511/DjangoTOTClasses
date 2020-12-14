from django.urls import path
from .views import addStudent,read,update,delete


urlpatterns = [
path('addStudent/',addStudent,name='addStudent'),
path('read/',read,name='read'),
path('update/<int:id>',update,name="update"),
path('delete/<int:id>',delete,name='delete')
]