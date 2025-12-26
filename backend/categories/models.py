from django.db import models

class Category(models.Model):
    name_ar = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    icon = models.ImageField(upload_to='category_icons/', null=True, blank=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return f"{self.name_en} / {self.name_ar}"