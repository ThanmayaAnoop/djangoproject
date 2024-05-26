from django.shortcuts import render

def hotel_login(request):
    return render(request, 'hotel_app/login.html')
