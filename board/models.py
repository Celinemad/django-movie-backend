from django.db import models
from accounts.models import CustomUser

# class Movie(models.Model):
#     title_kor = models.CharField(max_length=100)
#     title_eng = models.CharField(max_length=100)
#     poster_url = models.CharField(max_length=200, blank = False)
#     rating_aud = models.CharField(null=True, max_length=100)
#     rating_cri = models.CharField(null=True, max_length=100)
#     rating_net = models.CharField(null=True, max_length=100)
#     genre = models.CharField(null=True, max_length=100)
#     showtimes = models.CharField(null=True, max_length=100)
#     release_date = models.CharField(null=True, max_length=100)
#     rate = models.CharField(null=True, max_length=100)
#     summary = models.TextField(default="")
#     # staffs = models.ForeignKey(Staff, null=True, on_delete=models.CASCADE)
#     # staff = models.ManyToManyField(Staff) 
#     # staff = models.ForeignKey(Staff, null=True, on_delete=models.CASCADE)
#     # staff = models.ManyToManyField(Staff, blank=True)

#     def __str__(self):
#         return self.title_kor



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
    # staff = models.ManyToManyField(Staff) 
    # staff = models.ForeignKey('board.Staff', null=True, on_delete=models.CASCADE, related_name='movies')
    # staff = models.ManyToManyField(self.board.Staff, blank=True)

    def __str__(self):
        return self.title_kor

class Staff(models.Model):
    movie_id = models.ForeignKey(MovieList, null=True,on_delete=models.CASCADE, related_name='staff') #related_name='movie_id'
    name = models.TextField(default="")
    role = models.TextField(default="")
    image_url = models.TextField(default="")

    def __str__(self):
        return self.name
    
class Comment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()

# class MovieDetail(models.Model):
#     # user = models.ForeignKey(CustomUser, null=True, on_delete=models.CASCADE)
#     title_kor = models.CharField(null=True, max_length=100)
#     title_eng = models.CharField(null=True, max_length=100)
#     poster_url = models.CharField(null=True, max_length=256)
#     rating_aud = models.CharField(null=True, max_length=100)
#     rating_cri = models.CharField(null=True, max_length=100)
#     rating_net = models.CharField(null=True, max_length=100)
#     genre = models.CharField(null=True, max_length=100)
#     showtimes = models.CharField(null=True, max_length=100)
#     release_date = models.CharField(null=True, max_length=100)
#     rate = models.CharField(null=True, max_length=100)
#     summary = models.TextField(default="")
#     # staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
#     staff = models.ManyToManyField(Staff)

#     def __str__(self):
#         return self.title_kor
