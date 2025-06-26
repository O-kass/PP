from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path("game1.html/", views.load_pyfile_function)
]