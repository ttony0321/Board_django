from django.urls import path
from . import views

app_name = 'board'
urlpatterns = [
    path('', views.BoardListView.as_view(), name='board_list'),
    path('<int:pk>/', views.board_detail_view, name='board_detail'),#게시글 상세보기
    path('write/', views.board_write_view, name='board_write'),
]