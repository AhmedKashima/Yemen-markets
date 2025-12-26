from django.core.management.base import BaseCommand
from locations.models import Governorate, City

class Command(BaseCommand):
    help = 'Loads ALL 22 Yemen Governorates'

    def handle(self, *args, **kwargs):
        # Full List of 22 Governorates (Official)
        data = [
            {"en": "Sana'a City", "ar": "أمانة العاصمة", "slug": "amanat-al-asimah"},
            {"en": "Sana'a", "ar": "محافظة صنعاء", "slug": "sanaa-gov"},
            {"en": "Aden", "ar": "عدن", "slug": "aden"},
            {"en": "Taiz", "ar": "تعز", "slug": "taiz"},
            {"en": "Al Hudaydah", "ar": "الحديدة", "slug": "hudaydah"},
            {"en": "Ibb", "ar": "إب", "slug": "ibb"},
            {"en": "Abyan", "ar": "أبين", "slug": "abyan"},
            {"en": "Dhamar", "ar": "ذمار", "slug": "dhamar"},
            {"en": "Hajjah", "ar": "حجة", "slug": "hajjah"},
            {"en": "Amran", "ar": "عمران", "slug": "amran"},
            {"en": "Al Bayda", "ar": "البيضاء", "slug": "bayda"},
            {"en": "Sa'dah", "ar": "صعدة", "slug": "sadah"},
            {"en": "Lahij", "ar": "لحج", "slug": "lahij"},
            {"en": "Hadhramaut", "ar": "حضرموت", "slug": "hadhramaut"},
            {"en": "Al Mahwit", "ar": "المحويت", "slug": "mahwit"},
            {"en": "Al Mahrah", "ar": "المهرة", "slug": "mahrah"},
            {"en": "Ma'rib", "ar": "مأرب", "slug": "marib"},
            {"en": "Raymah", "ar": "ريمة", "slug": "raymah"},
            {"en": "Shabwah", "ar": "شبوة", "slug": "shabwah"},
            {"en": "Al Jawf", "ar": "الجوف", "slug": "jawf"},
            {"en": "Al Dhale'e", "ar": "الضالع", "slug": "dhalea"},
            {"en": "Socotra", "ar": "سقطرى", "slug": "socotra"},
        ]

        # Basic placeholder cities for logic to work (You can add more later)
        common_cities = ["City Center", "North District", "South District"]

        for gov_data in data:
            gov, created = Governorate.objects.get_or_create(
                slug=gov_data['slug'],
                defaults={'name_en': gov_data['en'], 'name_ar': gov_data['ar']}
            )
            
            # If Gov exists, update names just in case
            if not created:
                gov.name_en = gov_data['en']
                gov.name_ar = gov_data['ar']
                gov.save()

            # Add default city for testing if none exist
            if gov.cities.count() == 0:
                for i, city_en in enumerate(common_cities):
                    City.objects.create(
                        name_en=f"{gov_data['en']} - {city_en}",
                        name_ar=f"{gov_data['ar']} - مركز", # Placeholder Arabic
                        slug=f"{gov_data['slug']}-{i}",
                        governorate=gov
                    )

        self.stdout.write(self.style.SUCCESS('✅ All 22 Governorates Loaded'))