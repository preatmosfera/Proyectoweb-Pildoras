from django.shortcuts import render
from blog.models import Post, Categoria

# Create your views here.
def blog(request):
    posts=Post.objects.all()
    return render(request, "blog/blog.html", {"posts": posts})

"""def blog(request):
    posts = Post.objects.all()
    categorias = set()

    # Iterar sobre los posts para recolectar categorías únicas
    for post in posts:
        for categoria in post.categorias.all():
            if categoria.id:  # Asegurarse de que el id de la categoría sea válido
                categorias.add(categoria)
    
    return render(request, "blog/blog.html", {"posts": posts, "categorias": categorias})"""


def categoria(request, categoria_id):
    categoria=Categoria.objects.get(id=categoria_id)
    posts=Post.objects.filter(categorias=categoria)
    return render(request, "blog/categoria.html", {'categoria': categoria, "posts": posts})