from django.urls import path
from .views import index, books, delete, update

urlpatterns = [
    path('',index,name='index' ),
    path('books/', books,name='books' ),
    path('delete/<int:id>',delete, name='delete' ),
    path('update/<int:id>',update, name='update' ),
]
