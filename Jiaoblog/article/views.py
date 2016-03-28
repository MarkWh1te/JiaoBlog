from django.shortcuts import render_to_response,get_object_or_404
from django.template import Template,Context
from django.views.generic.detail import DetailView

import models
# Create your views here.


def Post_list(request):
    posts = models.Post.objects.all()
    return render_to_response("post_list.html",{"posts":posts})


class Post_detail(DetailView):
    def get_object(self):
        return get_object_or_404(models.Post,pk=self.kwargs.get('pk',None))

   
