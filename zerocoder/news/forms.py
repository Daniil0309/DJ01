from .models import News_post
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea
class News_postForm(ModelForm):
    class Meta:
        model = News_post
        fields = ['user_name', 'title', 'short_description', 'text', 'pub_date']
        widgets = {
            'user_name': TextInput(attrs={'class': 'form-control'}),
            'title': TextInput(attrs={'class': 'form-control'}),
            'short_description': TextInput(attrs={'class': 'form-control'}),
            'text': Textarea(attrs={'class': 'form-control'}),
            'pub_date': DateTimeInput(attrs={'class': 'form-control'}),
        }
