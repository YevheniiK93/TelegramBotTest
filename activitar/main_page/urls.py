from django.urls import path, include
from .views import main_page_view

app_name = 'main_page'

urlpatterns = [
    path('', main_page_view)
    ]
