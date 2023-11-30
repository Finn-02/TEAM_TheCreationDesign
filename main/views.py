from django.shortcuts import render

# Create your views here.
def landing(request):
    return render(request, 'main/LandingPage_BL.html')

# def login(request):
#     return render(request, 'main/Login.html')

def signup(request):
    return render(request, 'main/Signup.html')

def test(request):
    return render(request, 'index.html')