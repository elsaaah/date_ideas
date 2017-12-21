from rest_framework import serializers
from dateideas.models import Ideas
from django.utils import timezone


class IdeaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ideas
        fields = ('id', 'date', 'costs', 'created_date', 'published_date', 'keyword')
    id = serializers.IntegerField(read_only=True)
    date = serializers.CharField(max_length=200)
    costs = serializers.DecimalField(max_digits=8, decimal_places=2, default=0)
    created_date = serializers.DateTimeField(default=timezone.now)
    published_date = serializers.DateTimeField(default=timezone.now)
    keyword = serializers.CharField(max_length=200)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Ideas.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.date = validated_data.get('date', instance.date)
        instance.costs = validated_data.get('costs', instance.costs)
        instance.created_date = validated_data.get('created_date', instance.created_date)
        instance.published_date = validated_data.get('published_date', instance.published_date)
        instance.keyword = validated_data.get('keyword', instance.keyword)
        instance.save()
        return instance
