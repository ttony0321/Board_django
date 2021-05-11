from django.shortcuts import render
from django.views.generic import ListView
from .models import Board
from django.contrib import messages
from django.db.models import Q
from user.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from .forms import BoardWriteForm
from user.models import User
# Create your views here.

class BoardListView(ListView):
    model = Board
    paginate_by = 5#한페이지에 표시할 갯수
    template_name = 'board/board_list.html'
    context_object_name = 'board_list'

    def get_queryset(self):
        board_list = Board.objects.order_by('-id')
        return board_list

    # 검색 타입, keyword, search_type 계속 유지하는 소스
    def get_context_data(self, **kwargs):       #페이지네이터 기능
        context = super().get_context_data(**kwargs)
        paginator = context['paginator']
        page_numbers_range = 5
        max_index = len(paginator.page_range)

        page = self.request.GET.get('page')
        current_page = int(page) if page else 1

        start_index = int((current_page - 1)/page_numbers_range) * page_numbers_range
        end_index = start_index + page_numbers_range
        if end_index >= max_index:
            end_index = max_index

        page_range = paginator.page_range[start_index:end_index]
        context['page_range'] = page_range

        search_keyword = self.request.GET.get('q', '')
        search_type = self.request.GET.get('type', '')
        if len(search_keyword) > 1:
            context['q'] = search_keyword
        context['type'] = search_type

        return context

#게시글 검색 기능 구현

def get_queryset(self):
    board_list = Board.objects.order_by('-id')
    search_keyword = self.request.GET.get('q', '')
    search_type = self.request.GET.get('type', '')

    if search_keyword:
        if len(search_keyword) > 1:
            if search_type == 'all':
                search_board_list = board_list.filter(Q(title__icontains=search_keyword) | Q(content__icontains=search_keyword) | Q(writer__userid__icontains=search_keyword))
            elif search_type == 'title_content':
                search_board_list = board_list.filter(Q(title__icontains=search_keyword) | Q(content__icontains=search_keyword))
            elif search_type == 'title':
                search_board_list = board_list.filter(title__icontains=search_keyword)
            elif search_type == 'content':
                search_board_list = board_list.filter(content__icontains=search_keyword)
            elif search_type == 'writer':
                search_board_list = board_list.filter(writer__userid__icontains=search_keyword)

            return search_board_list
        else:
            messages.error(self.request, '검색어는 2글자 이상 입력해주세요.')
    return board_list




#게시글 상세보기
@login_required
def board_detail_view(request, pk):
    board = get_object_or_404(Board, pk=pk)
    session_cookie = request.session['userid']#session_cookie 에 로그인한 아이디 삽입
    cookie_name = F'board_hits:{session_cookie}'#cookie_name 에 session_cookie으로 접속한 사용자 아이디 삽입
    context = {
        'board': board,
    }
    response = render(request, 'board/board_detail.html', context)

    #조회수 중복 방지 구현
    if request.COOKIES.get(cookie_name) is not None:
        cookies = request.COOKIES.get(cookie_name)#쿠키생성
        cookies_list = cookies.split('|')#로그인하면 쿠키들은 cookies_list 에 삽입
        if str(pk) not in cookies_list:
            response.set_cookie(cookie_name, cookies + f'|{pk}', expires=None)
            board.views += 1
            board.save()
            return response
    else:
        response.set_cookie(cookie_name, pk, expires=None)
        board.views += 1
        board.save()
        return response
    return render(request, 'board/board_detail.html', context)

#게시글 작성하기
@login_required
def board_write_view(request):
    if request.method == 'POST':
        form = BoardWriteForm(request.POST)
        user = request.session['userid']
        userid = User.objects.get(userid=user)

        if form.is_valid():
            board = form.save(commit=False)
            board.writer = userid
            board.save()
            return redirect('board:board_list')
    else:
        form = BoardWriteForm()

    return render(request, "board/board_write.html", {'form':form})