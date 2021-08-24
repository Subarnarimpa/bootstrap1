from django.shortcuts import render

# Create your views here.
def app1_func(request):
    return render(request,'app1_cdn.html')
