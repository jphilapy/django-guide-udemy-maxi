from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def monthly_challenges(request, month):
    if month == "january":
        challenge_text = "challenge of " + month
    elif month == "february":
        challenge_text = "challenge of " + month
    elif month == "march":
        challenge_text = "challenge of " + month
    elif month == "april":
        challenge_text = "challenge of " + month
    elif month == "may":
        challenge_text = "challenge of " + month
    else:
        return HttpResponse("This month is not supported.")
    return HttpResponse(challenge_text)
