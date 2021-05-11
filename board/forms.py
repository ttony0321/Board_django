from django import forms
from .models import Board


class BoardWriteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BoardWriteForm, self).__init__(*args, **kwargs)
        self.fields['title'].label ='제목'
        self.fields['title'].widget.attrs.update({
            'placeholder':'제목을 입력해주세요',
            'class': 'form-control',
            'autofocus': True,
        })

    class Meta:
        model = Board
        fields = ['title', 'content', 'top_fixed']