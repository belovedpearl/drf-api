from django.db import IntegrityError
from rest_framework import serializers
from likes.models import Like


class LikeSerializer(serializers.ModelSerializer):
    """
    Serializer for the Like model
    The create method handles the unique constraint on 'owner' and 'post'
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Like
        fields = ['id', 'created_at', 'owner', 'post']

    def create(self, validated_data):
    """
    Prevent double duplication of likes
    stops the integrity error page loading
    """
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError(
                {'details': 'Possible Duplicate'}
            )