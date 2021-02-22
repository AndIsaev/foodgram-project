from rest_framework import serializers
from recipes.models import Purchase


class PurchaseSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    recipe = serializers.StringRelatedField()

    class Meta:
        fields = '__all__'
        model = Purchase

    def validate(self, data):
        super().validate(data)
        user = self.context.get('request_user')
        recipe = self.context.get('id')
        if Purchase.objects.filter(user=user, recipe=recipe).exists():
            raise serializers.ValidationError('Already purchased')
        return data
