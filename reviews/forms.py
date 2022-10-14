from django import forms
from .models import Review
from django.utils.translation import gettext_lazy as _

class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        exclude = ('created_at','updated_at', 'writer', 'grade')
        labels = {
            'title': _('리뷰 제목'),
            'content': _('리뷰 내용'),
            'movie_name': _('영화 제목'),
            'grade': _('평점'),
        }