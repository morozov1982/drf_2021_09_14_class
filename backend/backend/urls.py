"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter  # , SimpleRouter

from library.views import AuthorViewSet, BiographyViewSet, BookViewSet
# from library.views import author_view, AuthorListView, AuthorRetrieveView

router = DefaultRouter()  # SimpleRouter()
# router.register('authors', AuthorViewSet, basename='author')
router.register('authors', AuthorViewSet, basename='author')  # можно указывать basename='authors' - имя модели
router.register('biography', BiographyViewSet)
router.register('books', BookViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/authors/', AuthorListView.as_view()),
    # path('api/authors/<int:pk>/', AuthorRetrieveView.as_view()),
    path('api/authors/kwargs/<str:first_name>/', AuthorViewSet.as_view({'get': 'list'})),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
]
