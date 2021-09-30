from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=46)
    last_name = models.CharField(max_length=46)
    birthday_year = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.birthday_year}'


class Biography(models.Model):
    text = models.TextField()
    author = models.OneToOneField(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Book(models.Model):
    title = models.CharField(max_length=46)
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=64)
    author = models.ForeignKey(Author, models.PROTECT)

    def __str__(self):
        return self.title
