from django.urls import path

from .views import AuthorViewSet

app_name = 'library'

urlpatterns = [
    path('', AuthorViewSet.as_view({'get': 'list'})),
]
