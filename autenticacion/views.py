from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout

# Create your views here.
class VRegistro(View):

    def get(self, request):
        form=UserCreationForm()
        return render(request, "registro/registro.html", {"form":form})

    def post(self, request):
        form=UserCreationForm(request.POST)
        if form.is_valid():
            usuario=form.save()

            login(request, usuario)
            return redirect("Home")
        else:
            return render(request, "registro/registro.html", {"form": form})  # Retorna los errores
        
def cerrar_sesion(request):
    logout(request)
    return redirect("Home")

       
