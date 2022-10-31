from django.shortcuts import render
from .models import*
# Create your views here.


def view_summernote(request):
    post_data = Post.objects.all().order_by('-id').first()
    context = {"form": post_data}
    return render(request, "index.html", context)
