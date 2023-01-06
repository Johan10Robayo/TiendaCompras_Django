from django.shortcuts import render,redirect
from contacto.forms import Formulario_contacto
from django.core.mail import EmailMessage
# Create your views here.
def contacto(request):
    formulario_contacto=Formulario_contacto()
    if request.method=='POST':
        formulario_contacto=Formulario_contacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre= request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")

            email=EmailMessage("Mensaje desde la app web Django","El usaurio con nombre {} con la dirección {} escribe lo siguiente: \n \n {}".format(nombre,email,contenido),"",["johan.robayo@unillanos.edu.co"],
                               reply_to=[email])
            try:
                email.send()
                return redirect("/contacto/?valido=")
            except:
                return redirect("/contacto/?novalido=")




    return render(request,'contacto.html',{'miFormulario':formulario_contacto})

