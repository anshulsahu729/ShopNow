<<<<<<< HEAD
# blog/models.py
from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model

User = get_user_model()

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    body = models.TextField()
    image = models.ImageField(upload_to="blog/", blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    published_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
=======
# from django.db import models
# from django.utils.text import slugify
# from django.utils import timezone

# class BlogPost(models.Model):
#     title = models.CharField(max_length=200)
#     slug = models.SlugField(unique=True, blank=True)
#     body = models.TextField()
#     image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
#     published_date = models.DateTimeField(default=timezone.now)
#     active = models.BooleanField(default=True)

#     class Meta:
#         ordering = ['-published_date']

#     def __str__(self):
#         return self.title

#     def save(self, *args, **kwargs):
#         if not self.slug:
#             self.slug = slugify(self.title)
#         super().save(*args, **kwargs)


from django.db import models
from django.utils.text import slugify
from django.utils import timezone

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    body = models.TextField()
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    published_date = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

>>>>>>> bde541a3eac834c2416b6f7a3c13774424a508cf
