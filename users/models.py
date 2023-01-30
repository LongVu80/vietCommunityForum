from django.db import models
from django.conf import settings
from posts.models import Post

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
    photo = models.ImageField(upload_to='users/%y/%m/%d', blank=True)

    def __str__(self):
        return self.user.username

    @property
    def num_posts(self):
        return Post.objects.filter(user=self).count()