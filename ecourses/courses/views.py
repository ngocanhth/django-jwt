from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
  #  return HttpResponse("e-courses app")
    return render(request, template_name = "index.html", context={"name":"Ngoc Anh"})
