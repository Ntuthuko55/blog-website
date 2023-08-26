from django.urls import path
from myApp.views import home,details,listAll,delete,update,create

app_name='myApp'

urlpatterns=[
    path('',home,name ="home"),
    path('details/<int:id>/',details,name = 'details'),
    path('list/',listAll,name="list"),
    path('delete/<int:id>/',delete,name="delete"),
    path('update/<int:id>/',update,name="update"),
    path('create/',create,name="create"),
]