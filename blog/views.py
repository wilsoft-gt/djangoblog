#importamos las librerias necesarias para nuestro proyecto
import os
from django.conf import settings
from django.shortcuts import render #<- para renderizar un template
from django.http import HttpResponse, HttpResponseRedirect #<- respuesta del servidor en plain text o redireccionamiento
from .models import blogposts, images #<- importar base de datos para usarla en las views
from django.contrib.auth import authenticate, login, logout #<- loguea y desloguea a un usuario, sumamente necesario para loggins
from django.contrib.auth.decorators import login_required #<- redirecciona el template al loggin info si no hay ningun usuario logueado

# Create your views here.

def main(request):
    return HttpResponse("main screen")

def blog(request):
    #tomo el username como texto para pasarlo al template como texno no como objeto
    usernamelog = str(request.user)

    #tomo todos los post y los paso a una lista iterable
    blogs = blogposts.objects.all()

    #renderizo el template con los argumentos o variables que continenen el username y los datos de los blogs
    return render(request, "blog/blog.html", {"blogposts": blogs, "usernamelog":usernamelog})

def blogEntry(request):
    #tomo el username como texto para pasarlo al template como texno no como objeto
    usernamelog = str(request.user)

    #tomo el id enviado desde el get request que sera el id del blog que quiero mostrar
    postId = request.GET.get("id")

    #tomo unicamente el post que fue requerido desde el template
    postGet = blogposts.objects.get(id=postId)
    
    #reenvio la information requerida del template para usarlo dentro del blog
    return render(request, "blog/blogpost.html", {"postGet": postGet, "usernamelog":usernamelog})

#@login_required creo que no necesita mucha explicaion pero esto hace que sea requerido loguearse antes de poder ver el view
#para usarlo se necesita en import en la linea NO. 6 de este documento
def createEntry(request):
    #tomo el username como texto para pasarlo al template como texno no como objeto
    usernamelog = str(request.user)

    #si no estoy enviando un formulario va a mostrar el template con el form vacio
    if request.method == "GET":
        #renderiza el template en blanco
        return render(request, "blog/createedit.html", {"usernamelog":usernamelog})
    #si se solicita el view como POST (envio de formulario), entonces voy a tomar los datos y guardarlos en la base de datos
    elif request.method == "POST":
        #blogposts es el objeto que es llamado desde mi model (database)
        newp = blogposts()
        #aca tomo todos los datos enviados desde el post (lo que esta dentro de entry es el name que fue dado al input dentro del form)
        postTitle = request.POST.get("entryTitle")
        postHeadImage = request.POST.get("entryImageHeader")
        postBody = request.POST.get("postBody")
        #asigno los datos a las bases de datos
        newp.post_title = postTitle
        newp.post_image_header = postHeadImage
        newp.post_body = postBody
        #guardo el nuevo post a la base de datos
        newp.save()
        #una vez se guarda muestra una entrada vacia
        return render(request, "blog/createedit.html", {"post": newp})

#@login_required creo que no necesita mucha explicaion pero esto hace que sea requerido loguearse antes de poder ver el view
#para usarlo se necesita en import en la linea NO. 6 de este documento

def resources(request):
    usernamelog = str(request.user)
    #si la pagina solo se solicita se muestra el template y se pasan los datos dentro de mi tabla de imagenes
    if request.method == "GET":
        imagenes = images.objects.all()
        return render(request, "blog/resources.html", {"imagenes": imagenes, "usernamelog":usernamelog})

    #si se envia datos al template entonces tomo los datos y los guardo en el servidor
    #en este caso necesito usar si o si la linea: enctype="multipart/form-data" en el form porque no estoy usando el modelform de django
    elif request.method == "POST":
        newImg = images()
        newImg.imagefile = request.FILES["newpic"]
        newImg.save()
        imagenes = images.objects.all()
        return render(request, "blog/resources.html", {"imagenes": imagenes})

#este es el sistema de loggin que se hereda de a linea NO. 5 de este documento
def logginview(request):
    #cuando se llama al loggin, el formulario autmaticamente manda el 
    # url de la pagina a donde se va a redireccionar si el logue es exitoso, 
    # en el caso de django este objeto es "next"
    next_url = request.GET.get('next')

    #si se envia la informacion de loggin (user, pass), autentificamos la informaicion recibida
    if request.method == "POST":
        #datos recibidos del template
        username = request.POST['username']
        password = request.POST['password']
        #autentica los datos recibidos
        user = authenticate(request, username=username, password=password)

        #user se vuelve los datos recibidos desde el template
        if user is not None:
            if next_url:
                #esta simple linea loguea al user si este existe
                login(request, user)
                #y renderiza el view desde el que fue llamado el loggin
                return HttpResponseRedirect(request.GET.get("next"))
                
        else:
            #si el loggin es incorrecto entonces tira un error
            return HttpResponse("<h1>Error authenticating your credentials</h1>") 
    else:
        #si la pagina solo se solicita (GET), entonces renderiza el loggin template
        return render(request, "blog/loggin.html")

#esto es muy muy simple, creo que no se necesita tanta explicacion
def logoutview(request):
    #como solo se puede loguear un user por sesion entonces solamente se necesita cerrar la sesion y ya
    logout(request)
    return HttpResponseRedirect("blog")

def removeresource(request):
    imagen = request.GET.get("img")
    imagen_db = images.objects.get(id=imagen)
    imagen_path = os.path.join(settings.MEDIA_ROOT, str(imagen_db.imagefile))
    os.remove(imagen_path)
    imagen_db.delete()
    return HttpResponseRedirect("resources")

def administration(request):
    usernamelog = str(request.user)
    imagenes = images.objects.all()
    return render(request, "blog/administration.html", {"imagenes": imagenes, "usernamelog":usernamelog})