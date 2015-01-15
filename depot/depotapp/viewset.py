from rest_framework import viewsets
from serializers import OrderSerializer
from models import *
# Create your views here.
class OrderViewSet(viewsets.ModelViewSet):
    """
    allow to browse and edit API endpoint
    """
    
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
