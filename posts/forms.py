from tkinter import Widget
from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={
                "class":"title",
                "placeholder":"제목을 입력해주세요"}),
            "content":forms.Textarea(attrs={
                "placeholder":"내용을 입력해주세요"
            })}

