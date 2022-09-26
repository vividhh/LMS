import re
from urllib import response
from django.shortcuts import render, redirect
from django.contrib.auth.models import auth, User 
from django.contrib import messages

from lms.serializers import BooksSerializer
from .models import Books, Orders, Member
from django.contrib.auth.decorators import login_required
from django.views import View
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response



class BooksView(APIView):
    def get(self,request):
        book_name= Books.objects.all()
        serializer = BooksSerializer(book_name, many = True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        bookname = request.POST['bookname']
        author = request.POST['author']
        price = request.POST['price']
        genre = request.POST['genre']
        image = request.FILES['image']

# Create your views here.
@login_required(login_url='login')
def index(request):
    total_users = User.objects.all().count()
    total_books = Books.objects.all().count()
    total_orders = Orders.objects.all().count()
    context = {
        'users': total_users,
        'books': total_books,
        'orders': total_orders,
    }
    return render(request, 'index.html', context)




def books(request):
    books = Books.objects.all()
    context = {'books': books}
    return render(request, 'books.html', context)

def addbook(request):
    if request.method == 'POST':
        bookname = request.POST['bookname']
        author = request.POST['author']
        price = request.POST['price']
        genre = request.POST['genre']
        image = request.FILES['image']

        if Books.objects.filter(book_name=bookname).exists():
            messages.info(request, 'Book name already exists')
            return redirect('addbook.html')

        else:
            new_book = Books(book_name=bookname, author=author, price=price, genre=genre, image=image)
            new_book.save()
            return redirect('books')
    else:
        return render(request, 'addbook.html')

def deletebook(request, pk):
    book = Books.objects.get(id=pk)
    book.delete()
    return redirect("books")

def edit_book(request, pk):
    book = Books.objects.get(id=pk)
    if request.method == 'POST':
        book_name = request.POST['book_name']
        author = request.POST['author']
        price = request.POST['price']
        genre = request.POST['genre']

        book.book_name = book_name
        book.author = author
        book.price = price
        book.genre = genre

        book.save()
        return redirect("books")
    else:
        return render(request, "edit_book.html", {'book': book})

def borrowbook(request, uid, bid):
    book = Books.objects.get(id=bid)
    user = User.objects.get(id=uid)

    new_order = Orders(ordered_book=book, user=user)
    new_order.save()
    return redirect("books")


def returnbook(request, pk):
    order = Orders.objects.get(id=pk)
    order.returned = True 
    order.save()
    return redirect("orders")

def users(request):
    users = Member.objects.all()
    context = {'users': users}
    return render(request, 'users.html', context)

def edit_user(request, pk):
    member = Member.objects.get(id=pk)
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        role = request.POST['role']

        member.firstname = firstname
        member.lastname = lastname
        member.email = email
        member.role = role

        member.save()
        return redirect("users")
    else:
        return render(request, "edit_user.html", {'member': member})

def deleteuser(request, pk):
    user = Member.objects.get(id=pk)
    user.delete()
    return redirect("users")

def orders(request):
    if request.user.is_staff:
        orders = Orders.objects.all()
    else:
        orders = Orders.objects.filter(user=request.user)
    context = {'orders': orders}
    return render(request, 'orders.html', context)

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is None:
            messages.info(request, 'Invalid credentials')
            return redirect('login')
        else:
            auth.login(request, user)
            return redirect('/')
           
    else:
        return render(request, 'login.html')

# def userIndex(request):

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        role = request.POST['role']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists')
                return redirect('signup')

            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already in use')
                return redirect('signup')

            else:
                user = User.objects.create_user(last_name=lastname, first_name=firstname, username=username, email=email, password=password)
                user.save()
                if role == 'Librarian':
                    user.is_staff = True
                    user.save()
                else:
                    new_member = Member(lastname=lastname, firstname=firstname, user=user, role=role, email=email, password=password) 
                    new_member.save()
                return redirect('login')
            
        else:
            messages.info(request, 'Password doesn\'t match')
            return redirect('signup')

    else:
        return render(request, 'signup.html')

def logout(request):
    auth.logout(request)
    return redirect('login')






    
