import graphene
from graphene_django import DjangoObjectType

from .models import Author, Book


class AuthorType(DjangoObjectType):
    class Meta:
        model = Author
        fields = '__all__'


class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = '__all__'


class Query(graphene.ObjectType):
    # hello = graphene.String(default_value='Hello!')
    all_authors = graphene.List(AuthorType)
    all_books = graphene.List(BookType)

    author_by_id = graphene.Field(AuthorType, id=graphene.Int(required=True), last_name=graphene.String())
    books_by_author_name = graphene.List(BookType, last_name=graphene.String(required=False))

    def resolve_all_authors(root, info):
        return Author.objects.all()

    def resolve_all_books(root, info):
        return Book.objects.all()

    def resolve_author_by_id(self, info, id, last_name=None):
        try:
            # if last_name:
            #     return Author.objects.get(last_name=last_name)
            return Author.objects.get(pk=id)
        except Author.DoesNotExist:
            return None

    def resolve_books_by_author_name(self, info, last_name=None):
        books = Book.objects.all()
        if last_name:
            books = Book.objects.filter(authors__last_name=last_name)
        return books


class AuthorCreateMutation(graphene.Mutation):
    class Arguments:
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        birthday_year = graphene.Int(required=True)

    author = graphene.Field(AuthorType)

    @classmethod
    def mutate(cls, root, info, first_name, last_name, birthday_year):
        author = Author(first_name=first_name, last_name=last_name, birthday_year=birthday_year)
        author.save()
        return AuthorCreateMutation(author)


class AuthorUpdateMutation(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        birthday_year = graphene.Int(required=True)

    author = graphene.Field(AuthorType)

    @classmethod
    def mutate(cls, root, info, id, birthday_year):
        author = Author.objects.get(pk=id)
        author.birthday_year = birthday_year
        author.save()
        return AuthorUpdateMutation(author)


class Mutations(graphene.ObjectType):
    create_author = AuthorCreateMutation.Field()
    update_author = AuthorUpdateMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutations)
