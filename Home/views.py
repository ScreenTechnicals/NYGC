from django.core.checks import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Greeting_Card
# Create your views here.

def home(request):      
    if not request.user.is_authenticated:
        return render(request, "Home/index.html")
    else:
        return redirect("/dashboard/")


def dashboard(request):
    if request.user.is_authenticated:    
        if request.method == "POST":
            sender = request.POST['sender']
            reciver = request.POST['reciver']
            user_id = request.POST['user_id']
            greeting_message = request.POST['greeting_message']
            greeting_card = Greeting_Card(user_id=user_id, sender=sender, reciver=reciver, greeting_message=greeting_message)
            greeting_card.save()
            return redirect("/dashboard/")
        greeting_cards = Greeting_Card.objects.filter(user_id=request.user.id).all()
        context = {
            'greeting_cards': greeting_cards,
        }
        return render(request, "Home/dashboard.html", context)
    else:
        return redirect("/")

def greeting_card(request, userID, greetID):
    greeting = Greeting_Card.objects.filter(id=greetID, user_id=userID).first()
    context = {
        'greeting':greeting,
    }
    return render(request, "Home/greeting_card.html", context)


def signup(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            username = request.POST['username']
            email = request.POST['email']
            pass1 = request.POST['pass1']
            pass2 = request.POST['pass2']
            if pass1 == pass2:
                user = User.objects.create_user(username, email, pass1)
                user.save()
                user_login = auth.authenticate(username=username, password=pass1)
                if user_login is not None:
                    auth.login(request, user_login)
                    messages.success(request, "Loged In Successfully !")
                    return redirect("/dashboard/")
            else:
                messages.warning(request, "Created Password and Confirmed password Don't Match Please Try Again !")

        return render(request, "Home/signup.html")
    else:
        return redirect("/dashboard/")

def login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            user_name = request.POST['user_name']
            password = request.POST['password']
            user = auth.authenticate(username=user_name, password=password)
            if user is not None:
                auth.login(request, user)
                messages.success(request, "Successfully Loged In!")
                return redirect("/dashboard/")
            else:
                messages.success(request, "User Does Not Exit!")
                return redirect("/login/")
                
        return render(request, "Home/login.html")
    else:
        return redirect("/dashboard")

def logout(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            auth.logout(request)
            return redirect("/login/")
    else:
        return redirect("/dashboard/")

