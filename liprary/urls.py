from django.urls import path
from .views import index, books, delete, update

urlpatterns = [
    path('index/',index ),
    path('books/', books),
    path('delete/',delete ),
    path('update/',update ),
]
