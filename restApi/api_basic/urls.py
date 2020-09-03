from django.urls import path
from api_basic.views import book_list

urlpatterns = [
    path('book/', book_list),
]