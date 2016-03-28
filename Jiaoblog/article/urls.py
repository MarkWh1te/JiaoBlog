
from django.conf.urls import url
import views

urlpatterns = [
        url(r'postlist/$',
                views.Post_list,
                name = "post_list"
                ),
        url(r'(?P<pk>\d+)/$',
            views.Post_detail.as_view(),
            name = "Post_detail"
            )
       ] 
