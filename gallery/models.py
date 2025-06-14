from django.db import models
from django.utils.text import slugify
from django.urls import reverse

class SiteSettings(models.Model):
    """Model for storing site-wide settings like site name, background image, logo, and social media links."""
    site_name = models.CharField(max_length=100, default="StyleHub")
    background_image = models.ImageField(upload_to='backgrounds/', blank=True, null=True)
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)
    instagram_profile = models.URLField(blank=True, null=True, help_text="URL to Instagram profile")

    class Meta:
        verbose_name = "Site Settings"
        verbose_name_plural = "Site Settings"

    def __str__(self):
        return self.site_name

    @classmethod
    def get_site_settings(cls):
        """Get or create site settings."""
        site_settings, created = cls.objects.get_or_create(pk=1)
        return site_settings


class Collection(models.Model):
    """Model for collections that contain items."""
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    image = models.ImageField(upload_to='collections/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        """Generate slug from title if not provided."""
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Get URL for collection's detail view."""
        return reverse('collection', kwargs={'slug': self.slug})


class CollectionItem(models.Model):
    """Model for items within collections."""
    collection = models.ForeignKey(Collection, related_name='items', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    url = models.URLField()
    image = models.ImageField(upload_to='items/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
