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
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter  # , SimpleRouter
from rest_framework.authtoken.views import obtain_auth_token

from library.views import AuthorViewSet, BiographyViewSet, BookViewSet
# from library.views import author_view, AuthorListView, AuthorRetrieveView

router = DefaultRouter()  # SimpleRouter()
router.register('authors', AuthorViewSet, basename='author')  # можно указывать basename='authors' - имя модели
router.register('biography', BiographyViewSet)
router.register('books', BookViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/authors/', AuthorListView.as_view()),
    # path('api/authors/<int:pk>/', AuthorRetrieveView.as_view()),
    # path('api/authors/kwargs/<str:first_name>/', AuthorViewSet.as_view({'get': 'list'})),
    # re_path('^api/(?P<version>v\d)/authors/$', AuthorViewSet.as_view({'get': 'list'})),
    # path('api/authors/', AuthorViewSet.as_view({'get': 'list'})),
    path('api/authors/v1', include('library.urls', namespace='v1')),
    path('api/authors/v2', include('library.urls', namespace='v2')),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', obtain_auth_token),
    # path('api/', include(router.urls)),
]
