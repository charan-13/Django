from django.contrib import admin
from django.urls import path, include
from HelloWorldApp.views import hello_world

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello_world, name='hello_world'),
    path('', hello_world),  # Add this line for the default path
]


