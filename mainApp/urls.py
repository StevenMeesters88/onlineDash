from django.urls import path, include
from .views import index, show_data, build_dash

urlpatterns = [
    path('', index),
    path('show_files/', show_data, name='show_data'),
    path('build_dash/', build_dash, name='build_dash')
]
