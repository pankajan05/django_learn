from django.urls import path
from api_basic.views import book_list, book_detail

urlpatterns = [
    path('book/', book_list),
    path('detail/<int:pk>/', book_detail),
]