from .models import Post, Image, Comment, Reply
from django import forms


class PostCreateForm(forms.ModelForm):
    class Meta:
        
        model = Post
        fields = ('title', 'body', "categories", "tags")

class ImageForm(forms.ModelForm):
    images = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    class Meta:
        model = Image
        fields = ('images', 'caption',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body', 'posted_by')

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ('body', 'posted_by')
