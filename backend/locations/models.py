from django.db import models

class Governorate(models.Model):
    name_ar = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f"{self.name_en} / {self.name_ar}"

class City(models.Model):
    governorate = models.ForeignKey(Governorate, related_name='cities', on_delete=models.CASCADE)
    name_ar = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = "Cities"

    def __str__(self):
        return f"{self.name_en} ({self.governorate.name_en})"