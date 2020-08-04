from django.db import models
import uuid
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.

class book(models.Model):
    id=models.UUIDField(
        primary_key=True,
        default=uuid.uuid4(),
        editable=False
    )
    Name=models.CharField(max_length=200)
    author=models.CharField(max_length=200)
    Price=models.DecimalField(max_digits=6,decimal_places=2)
    cover=models.ImageField(upload_to='covers/',blank=True)

    class Meta:  # new
        permissions = [
            ('special_status', 'Can read all books'),
        ]

    def __str__(self):
        return self.Name

    def get_absolute_url(self):
        return reverse('book_detail',args=[str(self.id)])


class review(models.Model):
    book=models.ForeignKey(book,on_delete=models.CASCADE,related_name='reviews')
    review=models.CharField(max_length=255)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.review


