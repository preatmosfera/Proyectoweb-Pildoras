from django.shortcuts import render, redirect
from .forms import FormularioContacto
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def contacto(request):
    formulario_contacto=FormularioContacto()

    if request.method=="POST":
        formulario_contacto=FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")

             # Enviar el correo
            send_mail(
                subject=f"Nuevo mensaje de {nombre}",  # Asunto del correo
                message=f"Mensaje: {contenido}\n\nCorreo de contacto: {email}",  # Cuerpo del correo
                from_email="juancasco.neuquen@gmail.com",  # Dirección de envío
                recipient_list=["juancasco.neuquen@gmail.com"],  # Lista de destinatarios
                fail_silently=False,  # Lanza excepciones si hay errores
            )

           

            return redirect("/contacto/?valido")
            

    return render(request, "contacto/contacto.html", {"miFormulario": formulario_contacto})