from django.db import models
from django.conf import settings

class Ad(models.Model):
    CONDITION_CHOICES = [('new', 'New'), ('used', 'Used')]
    STATUS_CHOICES = [
        ('pending', 'Pending Approval'),
        ('active', 'Active'),
        ('rejected', 'Rejected'),
        ('sold', 'Sold')
    ]

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='ads')
    category = models.ForeignKey('categories.Category', on_delete=models.CASCADE)
    city = models.ForeignKey('locations.City', on_delete=models.CASCADE)
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    currency = models.CharField(max_length=3, default='YER') # Yemeni Rial
    condition = models.CharField(max_length=10, choices=CONDITION_CHOICES, default='used')
    
    # Images (We will handle multiple images via a separate model or JSON later, for now simplified)
    main_image = models.ImageField(upload_to='ads/', null=True, blank=True)
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title