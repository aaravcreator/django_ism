from django.urls import path
from .views import * 
urlpatterns = [
    path('calculator',calculator),
    path('',index),
    path('details/<int:id>/',tododetails),
    path('update/<int:id>/',updateTodo),
    path('delete/<int:id>',delete),
    path('register/',registration)
]
