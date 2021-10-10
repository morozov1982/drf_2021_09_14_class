from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient, APITestCase, APISimpleTestCase, APIRequestFactory, force_authenticate
from .models import Author, Biography
from .views import AuthorViewSet
from django.contrib.auth.models import User
from mixer.backend.django import mixer


class MixerTestCase(APITestCase):
    def test_author_list(self):
        author = mixer.blend(Author, birthday_year=1799)
        print(author)

    def test_biography(self):
        bio = mixer.blend(Biography, author__birthday_year=1799)
        author = Author.objects.get(id=bio.author.id)
        print(bio, author)

        # for _ in range(1000):
        #     mixer.blend(Biography, author__birthday_year=1799)


class AuthorTestCase(APITestCase):
    def setUp(self):
        self.admin = User.objects.create_superuser('admin', 'admin3@loc.com', '123')
        self.client.login(username='admin', password='123')

    def test_author_list(self):
        Author.objects.create(first_name='Александр', last_name='Пушкин', birthday_year=1799)
        res = self.client.get('/api/authors/')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)

        self.client.logout()
        res = self.client.get('/api/authors/')
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

    def test_author_post(self):
        res = self.client.post('/api/authors/', {
            'first_name': 'Александр', 'last_name': 'Пушкин', 'birthday_year': 1799
        })
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        author = Author.objects.get(id=res.data['id'])
        self.assertEqual(author.last_name, 'Пушкин')

    def test_factory(self):
        factory = APIRequestFactory()
        view = AuthorViewSet.as_view({'get': 'list'})
        request = factory.get('/api/authors/')
        res = view(request)
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

        request = factory.get('/api/authors/')
        force_authenticate(request, self.admin)
        res = view(request)
        self.assertEqual(res.status_code, status.HTTP_200_OK)


class FuncTest(APISimpleTestCase):
    def test_func(self):
        self.assertTrue(True)
