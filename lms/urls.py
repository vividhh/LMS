from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('books', views.books, name='books'),
    path('addbook', views.addbook, name='addbook'),
    path('editbook/<str:pk>', views.edit_book, name='edit_book'),   
    path('deletebook/<str:pk>', views.deletebook, name='deletebook'),       
    path('borrowbook/<str:uid>/<str:bid>', views.borrowbook, name='borrowbook'),       
    path('returnbook/<str:pk>', views.returnbook, name='returnbook'),       
    path('orders', views.orders, name='orders'),
    path('users', views.users, name='users'),
    path('edituser/<str:pk>', views.edit_user, name='edit_user'),   
    path('deleteuser/<str:pk>', views.deleteuser, name='deleteuser'),   
    path('delete_user/<str:pk>', views.deleteuser, name='delete_user'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logout, name='logout'),
    path('api',views.BooksView.as_view())
]
