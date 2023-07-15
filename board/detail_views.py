from .models import Staff, MovieList, Comment
from .serializers import MovieDetailSerializer, CommentSerializer
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView, ListAPIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny  
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsOwnerOrReadOnly
import requests

@api_view(["GET"])
def init_db(request):
    url = "https://api.hufs-likelion-movie.kro.kr/movies?format=json"
    res = requests.get(url)
    movies = res.json()['movies']
    for movie in movies:
        movie1 = MovieList()
        movie1.title_kor = movie['title_kor']
        movie1.title_eng = movie['title_eng']
        movie1.poster_url = movie['poster_url']
        movie1.rating_aud = movie['rating_aud']
        movie1.rating_cri = movie['rating_cri']
        movie1.rating_net = movie['rating_net']
        movie1.genre = movie['genre']
        movie1.showtimes = movie['showtimes']
        movie1.release_date = movie['release_date']
        movie1.rate = movie['rate']
        movie1.summary = movie['summary']
        
        movie1.save()

        staffset = movie['staff']
        for staff in staffset:
            staff1 = Staff()
            staff1.movie = movie1
            staff1.name = staff['name']
            staff1.role = staff['role']
            staff1.image_url = staff['image_url']
            staff1.save()

    return Response(status=status.HTTP_200_OK)

class MovieDetailView(RetrieveAPIView):
    serializer_class = MovieDetailSerializer
    #authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]
    # lookup_url_kwarg = 'id'

    def get_queryset(self):
        movie_id = self.kwargs.get('pk')
        return MovieList.objects.filter(id=movie_id)

class CommentsList(ListCreateAPIView):
    serializer_class = CommentSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        movie_id = self.kwargs.get('movie_id')
        return Comment.objects.filter(movie_id = movie_id)
    
    def perform_create(self, serializer):
        movie_id = self.kwargs.get('movie_id')
        if self.request.user.is_authenticated:
            user = self.request.user
            serializer.save(userName=user.username, movie_id=movie_id)

class CommentDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_class = [IsOwnerOrReadOnly]

