import logging
import time

from django.http import JsonResponse

# Create your views here.
from apps.app1 import models
from apps.app1.tasks import add, sleep

logger = logging.getLogger(__name__)

def health(request):

    return JsonResponse("health", safe=False)

def health1(request):

    a = models.Book2.objects.filter(name2="book2").select_related("book")
    c = models.Book2.objects.filter(name2="book2").select_related("book", "book__mail", "book__mail__person")

    b = a[0].book.mail
    d = c[0].book.mail

    return JsonResponse("health1", safe=False)
    # return HttpResponse("wer")


def create(request):
    bookname = request.GET.get("bookname")
    bookname2 = request.GET.get("bookname2")
    mailaddress = request.GET.get("mailaddress")
    personsex = request.GET.get("personsex")
    personage = request.GET.get("personage")
    person1 = models.Person.objects.create(sex=personsex, age=personage)
    mail1 = models.Mail.objects.create(address=mailaddress, person_id=person1.id)
    book1 = models.Book.objects.create(name=bookname, mail_id=mail1.id)
    book2 = models.Book2.objects.create(name2=bookname2, book_id=book1.id)
    logger.error("34")

    return JsonResponse("create", safe=False)
