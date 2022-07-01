from rest_framework import serializers
from . import models

class LinkSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('target_url', 'description', 'created_at', 'updated_at',)
        model = models.Link
