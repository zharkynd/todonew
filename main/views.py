from django.shortcuts import render, HttpResponse

def homepage(request):
    return HttpResponse("Hello world")


def test(request):
    return render(request,"test.html")
