from django.db import models

class Post(models.Model):
    text = models.TextField()  # stores message content

    def __str__(self):
        return self.text[:50]  # shows preview text in admin
