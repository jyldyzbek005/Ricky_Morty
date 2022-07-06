from rest_framework.viewsets import ModelViewSet

from .models import CustomUser
from .serializers import CustomerUserSerializers

class CustomUserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomerUserSerializers