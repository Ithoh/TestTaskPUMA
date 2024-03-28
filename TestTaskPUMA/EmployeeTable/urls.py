from django.urls import path

from . import views

# Needed if multiple views have similar names, to differentiate them
app_name = 'EmployeeTable'

urlpatterns = [
    path("", views.index, name="index"),
]