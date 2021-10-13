from rest_framework.relations import HyperlinkedRelatedField
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer

from .models import Author, Biography, Book


class AuthorSerializer(ModelSerializer):  # (HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class AuthorSerializerV2(ModelSerializer):  # (HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name']


class BiographySerializer(ModelSerializer):
    # author = AuthorSerializer()
    # author = HyperlinkedRelatedField(view_name='author-detail', read_only=True)

    class Meta:
        model = Biography
        fields = '__all__'


class BookSerializer(ModelSerializer):
    # authors = AuthorSerializer(many=True)

    class Meta:
        model = Book
        fields = '__all__'
