from django.db import models
from django.utils.text import slugify

class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    thumbnail = models.ImageField(upload_to='portfolio/thumbnails/')
    description = models.TextField()
    problem_solved = models.TextField()
    my_role = models.TextField()
    key_features = models.TextField(help_text="Enter as a bulleted list or comma separated.")
    tools_used = models.CharField(max_length=300)
    github_link = models.URLField(blank=True, null=True)
    playable_link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
