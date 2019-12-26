from rest_framework.routers import DefaultRouter
from cambasBlog.apps.blog.views import BlogViewSet


app_name = 'blog'

router = DefaultRouter()
router.register('posts', BlogViewSet, base_name='posts')

urlpatterns = []

urlpatterns += router.urls
