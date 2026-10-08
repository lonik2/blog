from django.db import models

# Create your models here.

class category(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

class post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField("category", related_name="posts")

    def __str__(self):
        return self.title

class comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author} on '{self.post}'"

class postmedia(models.Model):
    IMAGE, VIDEO, AUDIO = "image", "video", "audio"
    KIND_CHOICES = [(IMAGE, "Imagen"), (VIDEO, "Video"), (AUDIO, "Audio")]

    post = models.ForeignKey(post, on_delete=models.CASCADE, related_name="media")
    kind = models.CharField(max_length=10, choices=KIND_CHOICES, default=IMAGE)
    file = models.FileField(upload_to="posts/%Y/%m/")
    caption = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.get_kind_display()} de {self.post.title}"