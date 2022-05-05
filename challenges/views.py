from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def index(request):
   return HttpResponse("You've landed at the index page for app/challenges!")



def january(request):
   return HttpResponse("You've landed on January's challenge page!")

def february(request):
   return HttpResponse("You've landed on February's challenge page!")

def march(request):
   return HttpResponse("You've landed on March's challenge page!")

def april(request):
   return HttpResponse("You've landed on April's challenge page!")

def may(request):
   return HttpResponse("You've landed on May's challenge page!")

def june(request):
   return HttpResponse("You've landed on June's challenge page!")

def july(request):
   return HttpResponse("You've landed on July's challenge page!")

def august(request):
   return HttpResponse("You've landed on August's challenge page!")

def september(request):
   return HttpResponse("You've landed on September's challenge page!")

def october(request):
   return HttpResponse("You've landed on October's challenge page!")

def november(request):
   return HttpResponse("You've landed on November's challenge page!")

def december(request):
   return HttpResponse("You've landed on December's challenge page!")

