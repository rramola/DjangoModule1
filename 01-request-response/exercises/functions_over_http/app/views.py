from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse


# Create your views here.
def hey_you_view(request, name) -> HttpRequest:
    return HttpResponse(f"Hello, {name}!")


def age_in_view(request, end, birth):
    age = end - birth
    return HttpResponse(age)


def order_total_view(request, burgers, fries, drinks):
    burgers_total = float(burgers) * 4.5
    fries_total = float(fries) * 1.5
    drinks_total = float(drinks) * 1
    return HttpResponse(burgers_total + fries_total + drinks_total)
