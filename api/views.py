from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from api.serializers import PurchaseSerializer
from recipes.models import Purchase, Recipe


class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    permission_classes = (IsAuthenticated, )

    def perform_create(self, serializer):
        recipe = get_object_or_404(Recipe, id=self.request.data.get('id'))
        serializer = PurchaseSerializer(data=self.request.data, context={
            'request_user': self.request.user})
        serializer.is_valid(raise_exception=True)
        serializer.save(user=self.request.user, recipe=recipe)
        return Response({'success': True}, status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        recipe = get_object_or_404(Recipe, pk=kwargs['pk'])
        shop = get_object_or_404(
            Purchase,
            recipe=recipe,
            user=request.user)
        shop.delete()
        return Response({'success': True})
