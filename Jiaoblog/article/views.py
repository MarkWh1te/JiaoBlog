from django.shortcuts import render_to_response
from django.template import Template,Context
import models
# Create your views here.


def Post_list(request):
    posts = models.Post.objects.all()
    return render_to_response("post_list.html",{"posts":posts})
    

