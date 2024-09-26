from django.db import models

class AIImageGeneration(models.Model):
    description = models.TextField()
    generated_image = models.ImageField(upload_to='generated_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class IconGeneration(models.Model):
    icon_description = models.TextField()
    generated_icon = models.ImageField(upload_to='generated_icons/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class PDFGeneration(models.Model):
    content = models.TextField()
    generated_pdf = models.FileField(upload_to='generated_pdfs/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class VideoGeneration(models.Model):
    video_content = models.TextField()
    generated_video = models.FileField(upload_to='generated_videos/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class BackgroundGeneration(models.Model):
    bg_description = models.TextField()
    generated_background = models.ImageField(upload_to='generated_backgrounds/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class BackgroundRemoval(models.Model):
    original_image = models.ImageField(upload_to='uploaded_images/')
    removed_bg_image = models.ImageField(upload_to='removed_backgrounds/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class MockupNews(models.Model):
    headline = models.CharField(max_length=255)
    body = models.TextField()
    generated_mockup = models.ImageField(upload_to='news_mockups/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
