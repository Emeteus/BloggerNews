from django import forms
from .models import Blogger

class BloggerForm(forms.ModelForm):
    class Meta:
        model = Blogger
        fields = ['name', 'category', 'description', 'article_url', 'video_url']
