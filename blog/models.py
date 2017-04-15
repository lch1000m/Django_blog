from django.db import models

from django.core.urlresolvers import reverse


class Post(models.Model):
    title     = models.CharField(max_length=255)
    image     = models.FileField(null=True, blank=True)
    content   = models.TextField()
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blogs:detail', kwargs={'id': self.id})


    class Meta:
        ordering = ['-timestamp']
