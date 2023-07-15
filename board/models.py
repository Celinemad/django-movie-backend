from django.db import models
from accounts.models import CustomUser


class Staff(models.Model):
    # movie_id = models.ForeignKey(MovieList, null=True,on_delete=models.CASCADE, related_name='staffs') #related_name='movie_id'
    name = models.CharField(null=True, max_length=100)
    role = models.CharField(null=True, max_length=100)
    image_url = models.CharField(null=True, max_length=256)

    def __str__(self):
        return self.name

class MovieList(models.Model):
    title_kor = models.CharField(max_length=100)
    title_eng = models.CharField(max_length=100)
    poster_url = models.CharField(max_length=200, blank = False)
    rating_aud = models.CharField(null=True, max_length=100)
    rating_cri = models.CharField(null=True, max_length=100)
    rating_net = models.CharField(null=True, max_length=100)
    genre = models.CharField(null=True, max_length=100)
    showtimes = models.CharField(null=True, max_length=100)
    release_date = models.CharField(null=True, max_length=100)
    rate = models.CharField(null=True, max_length=100)
    summary = models.TextField(default="")
    # staffs = models.ForeignKey(Staff, null=True, on_delete=models.CASCADE)
    staff = models.ManyToManyField(Staff) 

    def __str__(self):
        return self.title_kor
    
class Comment(models.Model):
    user = models.ForeignKey(CustomUser, null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(default="")

    def __str__(self):
        return self.comment

class MovieDetail(models.Model):
    # user = models.ForeignKey(CustomUser, null=True, on_delete=models.CASCADE)
    title_kor = models.CharField(null=True, max_length=100)
    title_eng = models.CharField(null=True, max_length=100)
    poster_url = models.CharField(null=True, max_length=256)
    rating_aud = models.CharField(null=True, max_length=100)
    rating_cri = models.CharField(null=True, max_length=100)
    rating_net = models.CharField(null=True, max_length=100)
    genre = models.CharField(null=True, max_length=100)
    showtimes = models.CharField(null=True, max_length=100)
    release_date = models.CharField(null=True, max_length=100)
    rate = models.CharField(null=True, max_length=100)
    summary = models.TextField(default="")
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    comments = models.ForeignKey(Comment, on_delete=models.CASCADE)

    def __str__(self):
        return self.title_kor
    

