from django.shortcuts import render

# Create your views here.
def index(request):
    context = {'home':'home'}
    return render(request, "HOME.html",context)

def about_us(request):
    context = {'abouts_us':'about_us'}
    return render(request,'ABOUT_US.html',context)