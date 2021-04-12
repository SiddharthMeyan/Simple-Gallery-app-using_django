from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('view_photo/<str:pk>/',views.view_photo,name='view-photo'),
    path('add_photo',views.add_photo,name='add-photo'),
    path('category/<str:id>',views.category,name='category'), #<str:id> is used as model field catergory is a foregin key
]
