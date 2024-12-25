from django.urls import path
from .views import (
    home, ListFilmView, DetailFilmView, CritqueCreateView,CommentCreateView,
    CommentListView
) 
from django.contrib.auth.decorators import login_required
from .api_views import (
    FilmListCreateView, FilmDetailView,
    CritiqueListCreateView, CritiqueDetailView,
    CustomUserListView, CustomUserDetailView
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('home', home, name="home"),
    path('', ListFilmView.as_view(), name="listfilm"),
    path('critique/', login_required(CritqueCreateView.as_view()), name="critique"),
    path('comment/',login_required(CommentCreateView.as_view()), name="comment"),
    path('comment/liste',CommentListView.as_view(), name="commentlist"),
    path('detailfilm/<int:pk>/', DetailFilmView.as_view(), name="detailfilm"),
    
    path('api/films/', FilmListCreateView.as_view(), name='film-list-create'),
    path('api/films/<int:pk>/', FilmDetailView.as_view(), name='film-detail'),

    path('api/critiques/', CritiqueListCreateView.as_view(), name='critique-list-create'),
    path('api/critiques/<int:pk>/', CritiqueDetailView.as_view(), name='critique-detail'),

    path('api/utilisateurs/', CustomUserListView.as_view(), name='user-list'),
    path('api/utilisateurs/<int:pk>/', CustomUserDetailView.as_view(), name='user-detail'),
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
