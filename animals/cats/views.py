import django_filters
from rest_framework import viewsets, status, mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from cats.models import Kitty, Breed, KittyRating
from cats.permissions import IsOwnerOrReadOnly, ReadOnly
from cats.serializers import KittySerializer, BreedSerializer, \
    KittyRatingSerializer


class KittyViewSet(viewsets.ModelViewSet):
    queryset = Kitty.objects.all()
    serializer_class = KittySerializer
    permission_classes = (IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly)
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]

    def get_queryset(self):
        breed = self.request.query_params.get('breed')
        qs = Kitty.objects.all().select_related('breed', 'owner')
        if breed:
            return qs.filter(breed__name=breed)
        return qs


class BreedViewSet(mixins.ListModelMixin,
                   GenericViewSet):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
    permission_classes = (ReadOnly,)


class RatingViewSet(viewsets.ModelViewSet):
    queryset = KittyRating.objects.all()
    serializer_class = KittyRatingSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            data = serializer.initial_data

            kitten = Kitty.objects.filter(
                id=data['kitty']
            ).select_related('owner').prefetch_related('ratings')
            kitty = kitten.first()

            if request.user == kitty.owner:
                detail = {'detail': 'Нельзя оценивать собственных котят.'}
                return Response(data=detail,
                                status=status.HTTP_403_FORBIDDEN)

            kitty_ratings = kitty.ratings.all()
            is_user_rating = kitty_ratings.filter(owner=request.user)

            if is_user_rating:
                detail = {'detail': 'Нельзя оценивать несколько раз.'}
                return Response(data=detail,
                                status=status.HTTP_403_FORBIDDEN)
            serializer.save()
            return Response(data=serializer.data,
                            status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance,
                                         data=request.data,
                                         partial=partial)

        if serializer.is_valid():
            if instance.owner != request.user:
                detail = {'detail': 'Нельзя изменять чужую оценку.'}
                return Response(data=detail,
                                status=status.HTTP_403_FORBIDDEN)
            serializer.save()
            return Response(data=serializer.data,
                            status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.owner != request.user:
            detail = {'detail': 'Нельзя удалять чужую оценку.'}
            return Response(data=detail,
                            status=status.HTTP_403_FORBIDDEN)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
