from django.forms import ModelForm
from .models import Article

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ["title", "text"]
        exclude = ["updated_at", "created_at"]
        