from django.shortcuts import render

# Create your views here.
def whyUs(request):
    return render(request,'why.html')