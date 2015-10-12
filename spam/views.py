from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic.list import ListView
# from django.utils import timezone


class SpamListView(ListView):
    pass


def index(request):
    return HttpResponse('This is a spammy page. Is "spammy" even a word?')


def details(request, spam_id):
    return HttpResponse('You are viewing details on {}.'.format(spam_id))
