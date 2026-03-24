from django.urls import path
from contact import views

app_name = 'home'

urlpatterns = [
    path('',views.index, name='index' ),
]
