from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import messages
from django.shortcuts import redirect
app_name = 'board'
urlpatterns = [
    path('', views.BoardListView.as_view(), name='board_list'),
    path('<int:pk>/', views.board_detail_view, name='board_detail'),  # 게시글 상세보기
    path('write/', views.board_write_view, name='board_write'),
    path('<int:pk>/edit/', views.board_edit_view, name='board_edit'),
    path('<int:pk>/delete/', views.board_delete_view, name='board_delete'),
    path('download/<int:pk>', views.board_download_view, name='board_download'),
]


#media파일 접근 제한
def protected_file(request, path, document_root=None):
    messages.error(request, '접근불가')
    return redirect('/')


#urlpatterns에 Media File을 제공하는 패턴을 추가하고 protected_file 함수를 구현함으로써 url로 서버상의 MEDIA_ROOT에 접근하는것을 방지합니다.
urlpatterns += static(settings.MEDIA_URL, protected_file, document_root = settings.MEDIA_ROOT)