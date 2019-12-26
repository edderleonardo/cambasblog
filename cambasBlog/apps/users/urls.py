from django.urls import path
from .views import CreateUserView, LoginAPI, LogoutAPI, AuthorListView

app_name = 'user'

urlpatterns = [
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', LogoutAPI.as_view(), name='logout'),
    path('create/user/', CreateUserView.as_view(), name='create'),
    path('authors/', AuthorListView.as_view(), name='authors'),
]
