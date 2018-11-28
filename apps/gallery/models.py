import os

from django.db import models
from django.urls import reverse_lazy

from apps.event.models import Event
from website.utils.cache import invalidate_template_cache
from website.utils.forms import unique_slugify


class Album(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(
        max_length=255,
        blank=True,
        null=True,
        help_text='Leave empty/unchanged for default slug.')
    previous_db_id = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    thumbnail = models.ForeignKey('Image', related_name='thumbnail_of', blank=True, null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(editable=False, auto_now_add=True)
    updated_at = models.DateTimeField(editable=False, auto_now=True)
    event = models.ForeignKey(Event, blank=True, null=True, related_name='albums', on_delete=models.CASCADE)
    is_featured = models.BooleanField(default=False)

    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail
        try:
            return self.images.all()[0]
        except IndexError:
            return None

    def save(self, *args, **kwargs):
        unique_slugify(self, self.name)

        if self.is_featured:
            if self.pk:
                Album.objects.all().exclude(pk=self.pk).update(is_featured=False)
            else:
                Album.objects.all().update(is_featured=False)
            Image.objects.all().update(is_featured=False)
        super(Album, self).save(*args, **kwargs)
        invalidate_template_cache('featured_image')

    def get_absolute_url(self):
        return reverse_lazy('album-images', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name or str(self.event)


class Image(models.Model):
    file = models.ImageField(upload_to='images/')
    album = models.ForeignKey(Album, related_name='images', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(editable=False, auto_now_add=True)
    updated_at = models.DateTimeField(editable=False, auto_now=True)
    is_featured = models.BooleanField(default=False)

    @property
    def file_name(self):
        try:
            return os.path.basename(self.file.file.name)
        except IOError:
            return '-'

    @property
    def file_name_sans_ext(self):
        return os.path.splitext(self.file_name)[0]

    @property
    def title(self):
        return self.name or ''

    # def get_absolute_url(self):
    #     return reverse('view_image', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        if self.is_featured:
            if self.pk:
                Image.objects.all().exclude(pk=self.pk).update(is_featured=False)
            else:
                Image.objects.all().update(is_featured=False)
            Album.objects.all().update(is_featured=False)
        super(Image, self).save(*args, **kwargs)
        invalidate_template_cache('featured_image')

    def __str__(self):
        return self.name or self.file_name

# Create your models here.
