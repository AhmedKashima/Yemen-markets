# from rest_framework import viewsets, permissions, filters
# from django_filters.rest_framework import DjangoFilterBackend
# from .models import Ad
# from .serializers import AdSerializer

# class AdViewSet(viewsets.ModelViewSet):
#     serializer_class = AdSerializer
#     filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
#     # Filtering capabilities
#     filterset_fields = ['category__slug', 'city__slug', 'condition', 'price']
#     search_fields = ['title', 'description']
#     ordering_fields = ['price', 'created_at']

#     def get_queryset(self):
#         # Only show active ads to public, but all ads to owner
#         if self.action == 'list':
#             return Ad.objects.filter(status='active').order_by('-created_at')
#         return Ad.objects.all()

#     def get_permissions(self):
#         if self.action in ['create', 'update', 'partial_update', 'destroy']:
#             return [permissions.IsAuthenticated()]
#         return [permissions.AllowAny()]

from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Ad
from .serializers import AdSerializer

class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.filter(status='active').order_by('-created_at')
    serializer_class = AdSerializer
    
    # تفعيل محركات البحث والفلترة
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # الفلاتر الثابتة (الفئة والمدينة)
    filterset_fields = ['category', 'city']
    
    # البحث بالكلمات (في العنوان والوصف)
    search_fields = ['title', 'description']
    
    # الترتيب (حسب السعر أو التاريخ)
    ordering_fields = ['price', 'created_at']