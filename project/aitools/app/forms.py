from django import forms
from .models import AIImageGeneration, IconGeneration, PDFGeneration, VideoGeneration, BackgroundGeneration, BackgroundRemoval, MockupNews

class AIImageGenerationForm(forms.ModelForm):
    class Meta:
        model = AIImageGeneration
        fields = ['description', 'generated_image']

class IconGenerationForm(forms.ModelForm):
    class Meta:
        model = IconGeneration
        fields = ['icon_description', 'generated_icon']

class PDFGenerationForm(forms.ModelForm):
    class Meta:
        model = PDFGeneration
        fields = ['content', 'generated_pdf']

class VideoGenerationForm(forms.ModelForm):
    class Meta:
        model = VideoGeneration
        fields = ['video_content', 'generated_video']

class BackgroundGenerationForm(forms.ModelForm):
    class Meta:
        model = BackgroundGeneration
        fields = ['bg_description', 'generated_background']

class BackgroundRemovalForm(forms.ModelForm):
    class Meta:
        model = BackgroundRemoval
        fields = ['original_image', 'removed_bg_image']

class MockupNewsForm(forms.ModelForm):
    class Meta:
        model = MockupNews
        fields = ['headline', 'body', 'generated_mockup']
