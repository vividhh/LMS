from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta

# Create your models here.
class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, default="User")
    firstname = models.CharField(max_length=30, null=True)
    lastname = models.CharField(max_length=20, null=True)
    email = models.CharField(max_length=60)
    password = models.CharField(max_length=35)

    def __str__(self):
        return self.firstname + " " + self.lastname 

        
class Books(models.Model):
    book_name = models.CharField(max_length=100)
    author = models.CharField(max_length=40)
    price = models.FloatField()
    genre = models.CharField(max_length=35)
    image = models.ImageField(upload_to='media')

    class Meta:
        db_table = 'Books'

    def __str__(self):
        return self.book_name

    
        

class Orders(models.Model):
    ordered_book = models.ForeignKey(Books, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date_ordered = models.DateField(default=datetime.now())
    due_date = models.DateField(default=datetime.now() + timedelta(days=5))
    returned = models.BooleanField(default=False, null=True)

    def __str__(self):
        return self.ordered_book.book_name