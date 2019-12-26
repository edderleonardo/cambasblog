from django.urls import path
from .views import CountryList

app_name = 'core'

urlpatterns = [
    path('countries/', CountryList.as_view(), name='countries'),
]
