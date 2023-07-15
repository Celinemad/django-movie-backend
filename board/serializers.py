from rest_framework import serializers
from .models import *

class StaffSerializer(serializers.ModelSerializer):
    # movie_id = serializers.ReadOnlyField(source="movie_id.title_kor")

    class Meta:
        model = Staff
        fields = ['id', 'name', 'role', 'image_url']

class MovieListSerializer(serializers.ModelSerializer):
    staff = StaffSerializer(many=True)
    class Meta:
        model = MovieList
        fields = ['id', 'title_kor', 'title_eng', 'poster_url', 'rating_aud', 'rating_cri', 'rating_net', 'genre', 'showtimes', 'release_date', 'rate', 'summary', 'staff']

class CommentSerializer(serializers.ModelSerializer):
    created_at = serializers.CharField(format="%Y-%m-%d", read_only=True)
    user = serializers.CharField(source='user.nickname', read_only=True)
    
    class Meta:
        model = Comment
        fields = ['id', 'user', 'created_at', 'comment']



class MovieDetailSerializer(serializers.ModelSerializer):
    staff = StaffSerializer(many=True)
    comments = CommentSerializer(many=True)

    class Meta:
        model = MovieList
        fields = ['id', 'title_kor', 'title_eng', 'poster_url', 'rating_aud', 'rating_cri', 'rating_net', 'genre', 'showtimes', 'release_date', 'rate', 'summary', 'staff']    #'staffs', 'comments' 안넣음
        # read_only_fields = ['user']   #읽는 것만 가능
