from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer

from .models import Author, Biography, Book


class AuthorSerializer(HyperlinkedModelSerializer):  # (ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BiographySerializer(ModelSerializer):
    # author = AuthorSerializer()

    class Meta:
        model = Biography
        fields = '__all__'


class BookSerializer(ModelSerializer):
    authors = AuthorSerializer(many=True)

    class Meta:
        model = Book
        fields = '__all__'
