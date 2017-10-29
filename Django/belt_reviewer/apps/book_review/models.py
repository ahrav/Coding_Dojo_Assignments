from __future__ import unicode_literals

from django.db import models
from ..login_registration.models import User

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Book(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Author, related_name = 'books')

class ReviewManager(models.Manager):
    def validate_review(self, postData):
        errors = []
        if len(postData['book_title']) < 1 or len(postData['review']) < 3:
            errors.append('Book title and review are required fields')
        if not 'author' in postData and len(postData['new_author']) < 4:
            errors.append('new author nambes must contain 3 or more characters')
        return errors

    def create_review(self, cleanData, user_id):
        author = None
        if len(cleanData['new_author']) < 1:
            author = Author.objects.get(id=int(cleanData['author']))
        else:
            author = Author.objects.create(name=cleanData['new_author'])

        book = None
        if not Book.objects.filter(title=cleanData['book_title']):
            book = Book.objects.create(title = cleanData['book_title'], author=author)
        else:
            book = Book.objects.get(title=cleanData['book_title'])
        self.create(
            description = cleanData['review'],
            rating = cleanData['rating'],
            book = book,
            user = User.objects.get(id=user_id)
        )

    def recent_and_old(self):
        return (self.all().order_by('-created_at')[:3], self.all().order_by('-created_at'[3:]))

class Review(models.Model):
    description = models.TextField()
    rating = models.IntegerField(default=1)
    book = models.ForeignKey(Book, related_name = 'reviews')
    user = models.ForeignKey(User, related_name = 'user_reviews')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ReviewManager()
