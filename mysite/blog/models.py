from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse

# Models

class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length = 300)
    text = models.TextField()
    published_date = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse("post_list")

    def __str__(self):
        return self.title
