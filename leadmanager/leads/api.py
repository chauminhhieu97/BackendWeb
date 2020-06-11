from rest_framework import viewsets, permissions, filters
from .serializers import LeadSerializer, MovieSerializer, UserSerializer, TagSerializer, RatingSerializer, LinkSerializer
from .models import Lead, User, movie, tag, rating, link
#
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from snippets.models import Snippet
# from snippets.serializers import SnippetSerializer

# Lead Viewset


class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = LeadSerializer


class UserViewSet(viewsets.ModelViewSet):
    #  ^' Starts-with search.
    # '=' Exact matches.
    # '@' Full-text search. (Currently only supported Django's MySQL backend.)
    # '$' Regex search.
    queryset = User.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer
    # Search engine Django
    filter_backends = [filters.SearchFilter]
    search_fields = ['=username', '=email']
    ordering_fields = ['username', 'email']


class MovieViewSet(viewsets.ModelViewSet):
    queryset = movie.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = MovieSerializer

# Test


class TagViewSet(viewsets.ModelViewSet):
    queryset = tag.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TagSerializer


class LinkViewSet(viewsets.ModelViewSet):
    queryset = link.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = LinkSerializer


class RatingViewSet(viewsets.ModelViewSet):
    queryset = rating.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = RatingSerializer
