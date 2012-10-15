from django.shortcuts import render

prefix = 'app'

def index(request):
  return render(request, prefix + '/index.html')

