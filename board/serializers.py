from rest_framework import serializers
from .models import *

class StaffSerializer(serializers.ModelSerializer):
    # movie_id = serializers.ReadOnlyField(source="movie_id.title_kor")
    
    class Meta:
        model = Staff
        fields = ['id', 'movie_id', 'name', 'role', 'image_url']

class MovieListSerializer(serializers.ModelSerializer):
    # staff = StaffSerializer(many=True)
    class Meta:
        model = MovieList
        fields = ['id', 'title_kor', 'title_eng', 'poster_url', 'rating_aud', 'rating_cri', 'rating_net', 'genre', 'showtimes', 'release_date', 'rate', 'summary']

 
class CommentSerializer(serializers.ModelSerializer):
    userComment = serializers.CharField(source="comment")
    
    class Meta:
        model = Comment
        read_only_fields = ['userName']
        fields = ['userName', 'userComment']
        



class MovieDetailSerializer(serializers.ModelSerializer):
    staff = StaffSerializer(many=True)
    class Meta:
        model = MovieList
        fields = ['title_kor', 'title_eng', 'poster_url', 'rating_aud', 'rating_cri', 'rating_net', 'genre', 'showtimes', 'release_date', 'rate', 'summary', 'staff',]
