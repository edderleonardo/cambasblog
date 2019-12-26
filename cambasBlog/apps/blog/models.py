from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Blog(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    published = models.DateTimeField(auto_created=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blogs')

    def __str__(self):
        return self.title
