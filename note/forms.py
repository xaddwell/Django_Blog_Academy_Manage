from django import forms
from .models import Note


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('title', 'tag1', 'tag2', 'content', 'is_show')
        labels = {
            'title': '标题',
            'tag1': '标签1',
            'tag2': '标签2',
            'content': '正文内容',
            'is_show': '是否可见'
        }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'tag1': forms.TextInput(attrs={'class': 'form-control'}),
            'tag2': forms.TextInput(attrs={'class': 'form-control'}),

        }