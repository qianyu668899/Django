from django.core.urlresolvers import reverse
#from djangorestframework.views import View
#from djangorestframework.resources import ModelResource
from models import *
from rest_framework import serializers

class OrderSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    address = serializers.CharField(required=False)
    email = serializers.CharField(required=False)
    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Order.objects.create(**validated_data)

