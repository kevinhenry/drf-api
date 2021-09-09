from rest_framework import generics
from .serializers import PlogSerializer
from .models import Plog

# Create your views here.
class PlogList(generics.ListCreateAPIView):
    queryset = Plog.objects.all()
    serializer_class = PlogSerializer

class PlogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Plog.objects.all()
    serializer_class = PlogSerializer