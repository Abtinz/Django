from django.shortcuts import render,HttpResponse

# Create your views here.
def firstPage(request):
    return HttpResponse("Hello Django Abtin Zandi : 19 : Theran This is Home page for path test in django!")

def contact(request):
    return HttpResponse("Contact us : </br>GitHub : Abtinz  Email : NotAbtin@FakeEmail.com" )