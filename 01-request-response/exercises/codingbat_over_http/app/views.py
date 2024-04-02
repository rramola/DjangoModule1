from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse


def warmup_one_view(request, num):
    if num > 89 and num < 111 or num > 189 and num < 211:
        return HttpResponse(True)
    else:
        return HttpResponse(False)


def warmup_two_view(request, word):
    i = 1
    new_word = ""
    while i < len(word):
        for item in word:
            new_word = new_word + word[:i]
            i += 1
        return HttpResponse(new_word)


def warmup_three_view(request, word):
    cat = 0
    dog = 0
    i = 0
    x = 3
    while i < len(word):
        if word[i:x] == "cat":
            cat += 1
        if word[i:x] == "dog":
            dog += 1
        i += 1
        x += 1
    if cat == dog:
        return HttpResponse(True)
    else:
        return HttpResponse(False)


def warmup_four_view(request, num1, num2, num3):
    total = num1 + num2 + num3

    if num1 == num2:
        total -= (num1 + num2)
    if num2 == num3:
        total -= (num2 + num3)
    if num1 == num3:
        total -= (num1 + num3)
    if num1 == num2 and num1 == num3:
        total = 0

    return HttpResponse(total)
