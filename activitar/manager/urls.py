from django.urls import path
from .views import submit_list, submit_update

app_name = 'manager'

urlpatterns = [
    path('submits/', submit_list, name='submits'),
    path('submits/update/<int:pk>', submit_update, name='submit_close'),
]