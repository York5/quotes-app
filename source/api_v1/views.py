from rest_framework.decorators import action
from rest_framework.mixins import UpdateModelMixin
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, permissions

from api_v1.serializers import QuoteSerializer, QuoteUpdateSerializer, QuoteRatingSerializer
from webapp.models import Quote, QUOTE_APPROVED


class LogoutView(APIView):
    permission_classes = []

    def post(self, request, *args, **kwargs):
        user = self.request.user
        if user.is_authenticated:
            user.auth_token.delete()
        return Response({'status': 'ok'})


class IsPostOrIsAuthenticated(permissions.BasePermission):

    def has_permission(self, request, view):
        # allow all POST requests
        if request.method == 'POST':
            return True
        # Otherwise, only allow authenticated requests
        return request.user and request.user.is_authenticated


class QuotesViewSet(viewsets.ModelViewSet):
    permission_classes = [IsPostOrIsAuthenticated | DjangoModelPermissionsOrAnonReadOnly]
    queryset = Quote.objects.none()

    def get_serializer_class(self):
        if self.action in ["update", "partial_update"]:
            return QuoteUpdateSerializer
        return QuoteSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Quote.objects.all().order_by('-created_at')
        else:
            return Quote.objects.filter(status='approved').order_by('-created_at')

    @action(methods=['post'], detail=True)
    def rate_up(self, request, pk=None):
        quote = self.get_object()
        if quote.status != QUOTE_APPROVED:
            return Response({'error': 'Цитата не утверждена'}, status=403)
        quote.rating += 1
        quote.save()
        return Response({'id': quote.pk, 'rating': quote.rating})

    @action(methods=['post'], detail=True)
    def rate_down(self, request, pk=None):
        quote = self.get_object()
        if quote.status != QUOTE_APPROVED:
            return Response({'error': 'Цитата не утверждена'}, status=403)
        quote.rating -= 1
        quote.save()
        return Response({'id': quote.pk, 'rating': quote.rating})





