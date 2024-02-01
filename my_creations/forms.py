from django import forms
from django.core.exceptions import ValidationError
from django.conf import settings
from .models import Creation


class CreationForm(forms.ModelForm):
    class Meta:
        model = Creation
        fields = ['title','text','video']

    # カスタムバリデーション

    def clean_video(self):
        video = self.cleaned_data.get('video')

        # ファイルサイズの制限 (10MB)
        if video.size > settings.MAX_UPLOAD_SIZE:
            raise ValidationError(f'ファイルの最大サイズは {settings.MAX_UPLOAD_SIZE // (1024 * 1024)}MBです。')

        # ファイル形式の制限 (MP4のみ)
        if not video.name.endswith('.mp4'):
            raise ValidationError('動画ファイルはMP4形式である必要があります。')

        return video

