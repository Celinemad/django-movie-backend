from django.urls import path
# from .views import *
from .detail_views import *
from .movielist_views import *

app_name = 'board'

urlpatterns = [
    path('', MovieListGet.as_view()),
    path('<int:pk>/', MovieDetailView.as_view()),    #pk값 아닌 movie 이름으로 변경
    path('staff/', StaffView.as_view()),
    path('call_list/', init_db),
    # path('', MovieListGet.as_view()),
]