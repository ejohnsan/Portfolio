from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

# from models import ContactoModel

# Create your views here.

def contacto(request):

    if request.method =="POST":

        subject=request.POST["asunto"]

        message=request.POST["contenido"] + " " + request.POST["email"]

        email_from=settings.EMAIL_HOST_USER

        recipient_list=["johnsandoval69@gmail.com"]

        send_mail(subject,message,email_from,recipient_list)
        messages.success(request, "Mensaje Enviado")
    
    return render(request, "contacto/form.html")




    


