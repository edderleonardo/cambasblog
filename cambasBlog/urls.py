from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('cambasBlog.apps.core.urls', namespace='core')),
    path('api/', include('cambasBlog.apps.users.urls', namespace='users')),
    path('api/', include('cambasBlog.apps.blog.urls', namespace='blog')),
    path('', include('cambasBlog.apps.index.urls', namespace='index')),

    path('docs/', get_swagger_view(title='CambasBlog API')),
]
