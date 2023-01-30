from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.shortcuts import reverse
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation
from taggit.managers import TaggableManager

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length= 400, unique=True, blank=True)
    description = models.TextField(default="description")

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    def get_url(self):
        return reverse("post", kwargs={
            "slug":self.slug
        })

    @property
    def num_posts(self):
        return Post.objects.filter(categories=self).count()

    @property
    def last_post(self):
        return Post.objects.filter(categories=self).latest("created")

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField(blank=True)
    categories = models.ManyToManyField(Category)
    slug = models.SlugField(max_length=200, blank=True)
    created = models.DateField(auto_now_add=True)
    liked_by = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="posts_liked", blank=True)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',
        related_query_name='hit_count_generic_relation'
    )
    tags = TaggableManager(blank=True)
    # comments = models.ManyToManyField(Comment, blank=True)
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            i = 1
            while Post.objects.filter(slug=self.slug).exists():
                self.slug = slugify(self.title) + '-' + str(i)
                i += 1
            super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_url(self):
        return reverse("detail", kwargs={
            "slug":self.slug
        })

    @property
    def num_comments(self):
        return self.comments.count()

    @property
    def last_reply(self):
        return self.comments.latest("created")

class Image(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')
    caption = models.TextField()
    images = models.ImageField(upload_to='images/%y/%m/%d', blank=True)
    def __str__(self):
        return self.post.title



class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    created = models.DateTimeField(auto_now=True)
    posted_by = models.CharField(max_length=100)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.body

    @property
    def num_comments(self):
        return self.body.count()

    @property
    def last_reply(self):
        return self.body.latest("created")

class Reply(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='replies')
    body = models.TextField()
    created = models.DateTimeField(auto_now=True)
    posted_by = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "replies"

    def __str__(self):
        return self.body

