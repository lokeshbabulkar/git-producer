from . import views
from django.urls import path
from.views import *
urlpatterns = [
  path('show/', show_details),
  path('create/', Add_empDetails),

]
