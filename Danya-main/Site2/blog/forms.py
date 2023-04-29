from django import forms
from blog.models import Post

class Postform(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text', 'image', 'category')