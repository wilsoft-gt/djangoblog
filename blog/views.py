# importamos las librerias necesarias para nuestro proyecto
import os
from django.conf import settings
from django.shortcuts import render  # <- para renderizar un template
# <- respuesta del servidor en plain text o redireccionamiento
from django.http import HttpResponse, HttpResponseRedirect
# <- importar base de datos para usarla en las views
from .models import blogposts, images, comment, User
# <- loguea y desloguea a un usuario, sumamente necesario para loggins
from django.contrib.auth import authenticate, login, logout
# <- redirecciona el template al loggin info si no hay ningun usuario logueado
from django.contrib.auth.decorators import login_required

# Create your views here.


def blog(request):
    # tomo el username como texto para pasarlo al template como texno no como objeto
    usernamelog = str(request.user)

    # tomo todos los post y los paso a una lista iterable
    blogs = blogposts.objects.order_by("-post_date")
    mostviewed = blogposts.objects.order_by("-post_views")[:5]
    mostcomments = blogposts.objects.order_by("-post_count_comments")[:5]

    # renderizo el template con los argumentos o variables que continenen el username y los datos de los blogs
    return render(request, "blog/blog.html", {"blogposts": blogs, "usernamelog": usernamelog, "views": mostviewed, "mostcommented": mostcomments})


def blogEntry(request, id):
    # tomo el username como texto para pasarlo al template como texno no como objeto
    usernamelog = str(request.user)

    # tomo unicamente el post que fue requerido desde el template
    postGet = blogposts.objects.get(id=id)
    userinfo = User.objects.get(username=postGet.post_author)
    comments = comment.objects.all().filter(
        comment_post=postGet).filter(comment_moderated=True)

    mostviewed = blogposts.objects.order_by("-post_views")[:5]
    mostcomments = blogposts.objects.order_by("-post_count_comments")[:5]

    postGet.post_views += 1
    postGet.save()
    if request.method == "POST":
        commentnew = comment()
        commentnew.comment_name = request.POST['comment_name']
        commentnew.comment_email = request.POST['comment_email']
        commentnew.comment_comment = request.POST['comment_body']
        commentnew.comment_post = postGet
        commentnew.save()
        postGet.post_count_comments = len(comments)
        postGet.save()
        if comments != "":
            return render(request, "blog/blogpost.html", {"postGet": postGet, "usernamelog": usernamelog, "comments": comments, "userinfo": userinfo, "views": mostviewed, "mostcommented": mostcomments})
        else:
            return render(request, "blog/blogpost.html", {"postGet": postGet, "usernamelog": usernamelog, "userinfo": userinfo, "views": mostviewed, "mostcommented": mostcomments})
    # reenvio la information requerida del template para usarlo dentro del blog
    else:
        if comments != "":
            return render(request, "blog/blogpost.html", {"postGet": postGet, "usernamelog": usernamelog, "comments": comments, "userinfo": userinfo, "views": mostviewed, "mostcommented": mostcomments})
        else:
            return render(request, "blog/blogpost.html", {"postGet": postGet, "usernamelog": usernamelog, "userinfo": userinfo, "views": mostviewed, "mostcommented": mostcomments})


# este es el sistema de loggin que se hereda de a linea NO. 5 de este documento


def logginview(request):
    # cuando se llama al loggin, el formulario autmaticamente manda el
    # url de la pagina a donde se va a redireccionar si el logue es exitoso,
    # en el caso de django este objeto es "next"
    next_url = request.GET.get('next')

    # si se envia la informacion de loggin (user, pass), autentificamos la informaicion recibida
    if request.method == "POST":
        # datos recibidos del template
        username = request.POST['username']
        password = request.POST['password']
        # autentica los datos recibidos
        user = authenticate(request, username=username, password=password)

        # user se vuelve los datos recibidos desde el template
        if user is not None:
            if next_url:
                # esta simple linea loguea al user si este existe
                login(request, user)
                # y renderiza el view desde el que fue llamado el loggin
                return HttpResponseRedirect(request.GET.get("next"))
            else:
                login(request, user)
                return HttpResponseRedirect("/")

        else:
            # si el loggin es incorrecto entonces tira un error
            return HttpResponse("<h1>Error authenticating your credentials</h1>")
    else:
        # si la pagina solo se solicita (GET), entonces renderiza el loggin template
        return render(request, "blog/loggin.html")

# esto es muy muy simple, creo que no se necesita tanta explicacion


def logoutview(request):
    # como solo se puede loguear un user por sesion entonces solamente se necesita cerrar la sesion y ya
    nextpost = request.GET.get("next")
    if nextpost:
        logout(request)
        return HttpResponseRedirect(nextpost)
    else:
        logout(request)
        return HttpResponseRedirect("/")


# ADMINISTRATION FOR BLOG ENTRIES


@login_required
def administration_entries(request):
    """DOCSTRING: administration_entries
        Returns the blog entries in the admin
    """
    entries = blogposts.objects.order_by("-post_date")
    return render(request, "blog/entries.html", {"entries": entries})


@login_required
def administration_create_entry(request):
    """DOCSTRING: adminisstration_create_entry
        Create a new blog post
    """
    if request.method == "POST":
        csrf, entryTitle, entryImageHeader, postBody = request.POST.values()
        blogposts.objects.create(
            post_title=entryTitle, post_image_header=entryImageHeader, post_body=postBody, post_author=request.user)
        return render(request, "blog/createedit.html")

    else:
        return render(request, "blog/createedit.html")


@login_required
def administration_delete_entry(request, id):
    """DOCSTRING: administration_delete_entry
        Delete the blog post
    """
    blogposts.objects.filter(pk=id).delete()
    return HttpResponseRedirect("/administracion")


def administration_update_entry(request, id):
    """DOCSTRING: administration_update_entry
        Update the blog post
    """
    if request.method == "POST":
        csrf, postTitle, postHeadImage, postBody = request.POST.values()
        blogposts.objects.filter(id=id).update(
            post_title=postTitle, post_image_header=postHeadImage, post_body=postBody)
        return HttpResponseRedirect(f"/post/{id}/update")
    else:
        posttoupdate = blogposts.objects.get(id=id)
        return render(request, "blog/createedit.html", {"entry": posttoupdate})

# ADMINISTRATION FOR COMMENTS ENTRIES


@login_required
def administration_comments(request):
    """DOCSTRING: administration_update_entry
        Update the blog post
    """
    comments = comment.objects.all()
    return render(request, "blog/comments.html", {"comments": comments})


@login_required
def administration_update_comment(request, id):
    if request.method == "POST":
        comment.objects.filter(pk=id).update(
            comment_moderated=request.POST['moderated'])
        return HttpResponseRedirect(f"/admnistration/comments")

    else:
        return HttpResponseRedirect(f"/admnistration/comments")


@login_required
def administration_delete_comment(request, id):
    comment.objects.filter(pk=id).delete()
    return HttpResponseRedirect(f"/administration/comments")

# ADMINISTRATION VIEW FOR RESOURCES


@login_required
def administration_resources(request):
    resources = images.objects.all()
    if request.method == "POST":
        images.objects.create(request.FILES["image"])
        return HttpResponseRedirect("/administration/resources")
    else:
        return render(request, "blog/resources.html", {"images": resources})


@login_required
def administration_delete_resource(request, id):
    imagen_db = images.objects.get(id=id)
    imagen_path = os.path.join(settings.MEDIA_ROOT, str(imagen_db.imagefile))
    os.remove(imagen_path)
    imagen_db.delete()
    return HttpResponseRedirect("/administration/resources")


@login_required
def resources(request):
    usernamelog = str(request.user)
    # si la pagina solo se solicita se muestra el template y se pasan los datos dentro de mi tabla de imagenes
    if request.method == "GET":
        imagenes = images.objects.all()
        return HttpResponseRedirect("administracion")

    # si se envia datos al template entonces tomo los datos y los guardo en el servidor
    # en este caso necesito usar si o si la linea: enctype="multipart/form-data" en el form porque no estoy usando el modelform de django
    elif request.method == "POST":
        images.objects.create(imagefile=request.FILES["newpic"])
        return HttpResponseRedirect("/administracion/resources")
