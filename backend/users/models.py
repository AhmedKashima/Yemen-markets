# from django.db import models

# # Create your models here.


from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _

class UserManager(BaseUserManager):
    def create_user(self, phone, password=None, **extra_fields):
        if not phone:
            raise ValueError('Users must have a phone number')
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(phone, password, **extra_fields)

class User(AbstractUser):
    username = None # Remove username field
    phone = models.CharField(_('Phone Number'), max_length=15, unique=True)
    full_name = models.CharField(max_length=100, blank=True)
    city = models.ForeignKey('locations.City', on_delete=models.SET_NULL, null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    
    # Yemen specific settings
    language = models.CharField(max_length=2, choices=[('ar', 'Arabic'), ('en', 'English')], default='ar')

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.phone