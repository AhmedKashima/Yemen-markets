from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.cache import cache
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken
import random

class RequestOTPView(APIView):
    """ Step 1: User sends phone, we generate code """
    def post(self, request):
        phone = request.data.get('phone')
        if not phone:
            return Response({'error': 'Phone number is required'}, status=400)

        # Generate 6-digit code
        otp = str(random.randint(100000, 999999))
        
        # Save to Redis Cache (expires in 5 minutes)
        # Key format: otp_96777000000
        cache.set(f'otp_{phone}', otp, timeout=300)

        # --- DEV ONLY: Print to Console ---
        print(f"\n🔥🔥🔥 YOUR LOGIN CODE IS: {otp} 🔥🔥🔥\n")
        # ----------------------------------

        return Response({'message': 'OTP sent (check server console)'})

class VerifyOTPView(APIView):
    """ Step 2: User sends code, we give JWT Token """
    def post(self, request):
        phone = request.data.get('phone')
        otp_input = request.data.get('otp')

        cached_otp = cache.get(f'otp_{phone}')

        if not cached_otp or cached_otp != otp_input:
            return Response({'error': 'Invalid or expired code'}, status=400)

        # Create or Get User
        user, created = User.objects.get_or_create(phone=phone)
        if created:
            user.is_active = True
            user.save()

        # Generate JWT Tokens
        refresh = RefreshToken.for_user(user)
        
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': {
                'id': user.id,
                'phone': user.phone,
                'is_new': created
            }
        })