from django.conf.urls import url
from .views import stub_view
from .views import list_view
from .views import detail_view
from .views import UserViewSet
from .views import viewsets
from rest_framework import routers
from myblog import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'cateogries', views.CategoryViewSet)
router.register(r'posts', views.PostViewSet)

urlpatterns = [
    url('', list_view, name="blog_index"),
    url('posts/(\d+)/$', detail_view, name="blog_detail"),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^accounts/', include('allauth.urls')),
]