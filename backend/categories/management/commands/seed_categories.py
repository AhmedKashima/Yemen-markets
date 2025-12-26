from django.core.management.base import BaseCommand
from categories.models import Category

class Command(BaseCommand):
    help = 'Seeds Categories'

    def handle(self, *args, **kwargs):
        cats = [
            {'id': 1, 'ar': 'مركبات', 'en': 'Vehicles', 'slug': 'vehicles'},
            {'id': 2, 'ar': 'عقارات', 'en': 'Real Estate', 'slug': 'real-estate'},
            {'id': 3, 'ar': 'إلكترونيات', 'en': 'Electronics', 'slug': 'electronics'},
            {'id': 4, 'ar': 'وظائف', 'en': 'Jobs', 'slug': 'jobs'},
        ]

        for c in cats:
            Category.objects.update_or_create(
                id=c['id'],
                defaults={
                    'name_ar': c['ar'],
                    'name_en': c['en'],
                    'slug': c['slug']
                }
            )
        
        self.stdout.write(self.style.SUCCESS('✅ Categories Seeded (IDs 1-4)'))