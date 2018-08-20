from .models import Speed
from rest_framework import serializers, viewsets


class SpeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Speed
        fields = '__all__'


class SpeedViewSet(viewsets.ModelViewSet):
    queryset = Speed.objects.all()
    serializer_class = SpeedSerializer
