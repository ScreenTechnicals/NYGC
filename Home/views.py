from django.core.checks import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Greeting_Card
# Create your views here.

def home(request):
    if request.user:
        return redirect("/dashboard/")

    return render(request, "Home/index.html")


def dashboard(request):
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

def greeting_card(request, userID, greetID):
    greeting = Greeting_Card.objects.filter(id=greetID, user_id=userID).first()
    context = {
        'greeting':greeting,
    }
    return render(request, "Home/greeting_card.html", context)


def signup(request):
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
                messages.warning(request, "Loged In Successfully !")
        else:
            messages.warning(request, "Created Password and Confirmed password Don't Match Please Try Again !")

    return render(request, "Home/signup.html")

def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect("/")

