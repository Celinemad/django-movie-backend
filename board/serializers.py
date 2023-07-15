from rest_framework import serializers
from .models import *

class StaffSerializer(serializers.ModelSerializer):
    # movie_id = serializers.ReadOnlyField(source="movie_id.title_kor")
    
    class Meta:
        model = Staff
        fields = ['id', 'movie_id', 'name', 'role', 'image_url']

class MovieListSerializer(serializers.ModelSerializer):
    staff = StaffSerializer(many=True)
    class Meta:
        model = MovieList
        fields = ['id', 'title_kor', 'title_eng', 'poster_url', 'rating_aud', 'rating_cri', 'rating_net', 'genre', 'showtimes', 'release_date', 'rate', 'summary', 'staff']
        
        # def to_representation(self, instance):
        #     representation = super().to_representation(instance)
        #     staff_data = representation.pop('staff')  # staff 필드 제거
        #     staff_list = []
        #     for staff in staff_data:
        #         staff_id = staff.pop('movie_id')  # staff의 movie_id 필드 제거
        #         staff['movie_id'] = staff_id['title_kor']  # staff의 movie_id 필드에 title_kor 값을 삽입
        #         staff_list.append(staff)
        #     representation['staff'] = staff_list  # 수정된 staff 필드 다시 삽입
        #     return representation

class CommentSerializer(serializers.ModelSerializer):
    # user = serializers.CharField(source='user.nickname', read_only=True)
    
    class Meta:
        model = Comment
        fields = ['id', 'user', 'created_at', 'comment']



class MovieDetailSerializer(serializers.ModelSerializer):
    staff = StaffSerializer(many=True)
    # comments = CommentSerializer(many=True)

    class Meta:
        model = MovieList
        fields = ['id', 'title_kor', 'title_eng', 'poster_url', 'rating_aud', 'rating_cri', 'rating_net', 'genre', 'showtimes', 'release_date', 'rate', 'summary', 'staff']    #'staffs', 'comments' 안넣음
        # read_only_fields = ['user']   #읽는 것만 가능
