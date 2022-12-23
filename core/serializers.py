from rest_framework import serializers

from core.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    subscribes = serializers.StringRelatedField(read_only=True, many=True)

    class Meta:
        model = Profile
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance
