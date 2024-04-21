from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from app.forms import WarmUpOneForm, WarmUpTwoForm
# def warmup_one_view(request, num):
#     if num > 89 and num < 111 or num > 189 and num < 211:
#         return HttpResponse(True)
#     else:
#         return HttpResponse(False)


# def warmup_two_view(request, word):
    # i = 1
    # new_word = ""
    # while i < len(word):
    #     for item in word:
    #         new_word = new_word + word[:i]
    #         i += 1
    #     return HttpResponse(new_word)


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


# def warmup_four_view(request, num1, num2, num3):
#     total = num1 + num2 + num3

#     if num1 == num2:
#         total -= (num1 + num2)
#     if num2 == num3:
#         total -= (num2 + num3)
#     if num1 == num3:
#         total -= (num1 + num3)
#     if num1 == num2 and num1 == num3:
#         total = 0

#     return HttpResponse(total)


def challenges(request):
    form = WarmUpOneForm(request.GET)
    form_two = WarmUpTwoForm(request.GET)
    if "num" in request.GET:
        answer = ""
        form = WarmUpOneForm(request.GET)
        if form.is_valid():
            num = form.cleaned_data["num"]
            if num > 89 and num < 111 or num > 189 and num < 211:  
                answer = "True"
            else:
                answer = "False"
            return render(request, "challenges.html", {"form": form, "answer": answer})
        else:
            return render(request, "challenges.html", {"form": form})
        
    if "string" in request.GET:
        form_two = WarmUpTwoForm(request.GET)
        if form_two.is_valid():
            string = form_two.cleaned_data["string"]
            i = 1
            new_word = ""
            while i < len(string):
                for letter in string:
                    new_word = new_word + string[:i]
                    i += 1
                return render(request, "challenges.html", {"form_two":form_two, "new_word": new_word})
        else:
            return render(request, "challenges.html", {"form_two": form_two})
    return render(request, "challenges.html", {"form_two": form_two, "form": form})

    #   cat = 0
    # dog = 0
    # i = 0
    # x = 3
    # while i < len(word):
    #     if word[i:x] == "cat":
    #         cat += 1
    #     if word[i:x] == "dog":
    #         dog += 1
    #     i += 1
    #     x += 1
    # if cat == dog:
    #     return HttpResponse(True)
    # else:
    #     return HttpResponse(False)

    
# def warm_up_two(request):
#     form_two = WarmUpTwpForm(request.GET)
#     if form_two.is_valid():
#         string = form_two.cleand_data["string"]
#         i = 1
#         new_word = ""
#         while i < len(word):
#             for letter in string:
#                 new_word = new_word + letter[:i]
#                 i += 1
#         return render(request, "home.html", {"form_two":form_two, "new_word": new_word})
#     else:
#         return render(request, "home.html", {"form_two": form_two})