from django.shortcuts import render

from .models import MovieList
from .serializers import MovieListSerializer

from rest_framework.response import Response
from rest_framework import status

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.generics import ListAPIView
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import AllowAny

class MovieListGet(ListAPIView):
    queryset = MovieList.objects.all()
    serializer_class = MovieListSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [AllowAny]

    # def get_queryset(self, request):
    #     search_keyword = self.request.GET.get('title', "") #post로 값이 들어와야 함 
    #     if search_keyword:
    #         movies = movies.filter(title__icontains=search_keyword)
    #         return render(request, {'movies':movies, 'q':search_keyword})

    paginate_by = 5

    # def perform_create(self, serializer):
    #     user = self.request.user
    #     serializer.save(user = user)

    # def get(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance)
    #     data = serializer.data
    #     data['staff'] = []  # 빈 리스트로 초기화
    #     return Response(data)
