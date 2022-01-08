from django.db import models


# Create your models here.

class Person(models.Model):
    sex = models.CharField(max_length=10, default="m")
    age = models.IntegerField(null=True)


class Mail(models.Model):
    address = models.CharField(max_length=30)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='mail', null=True)


class Book(models.Model):
    name = models.CharField(max_length=30)
    mail = models.ForeignKey(Mail, on_delete=models.CASCADE, related_name='book', null=True)


class Book2(models.Model):
    name2 = models.CharField(max_length=30)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book2', null=True)
