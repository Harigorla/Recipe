from django.shortcuts import render
from .models import Post


def createpost(request):
    if request.method == 'POST':
        if request.POST.get('title') and request.POST.get('content') and request.POST.get('feedback'):
            post = Post()
            post.title = request.POST.get('title')
            post.content = request.POST.get('content')
            post.feedback = request.POST.get('feedback')
            post.save()

            return render(request, 'create.html')

    else:
        return render(request, 'create.html')

