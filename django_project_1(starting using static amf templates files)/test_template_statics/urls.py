from django.urls import path
from .views import home_view, about_view

app_name = 'test'

urlpatterns = [
    path('', home_view,name = 'home'),
    path('about/', about_view, name = 'about'),
]