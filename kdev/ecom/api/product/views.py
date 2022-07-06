from rest_framework import viewsets


from .serializers import productSerializer
from .models import product
# Create your views here.

class productViewSet(viewsets.ModelViewSet):
    queryset = product.objects.all().order_by('id')
    serializer_class = productSerializer
