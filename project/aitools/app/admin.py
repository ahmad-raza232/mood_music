from django.contrib import admin
from .models import AIImageGeneration, IconGeneration, PDFGeneration, VideoGeneration, BackgroundGeneration, BackgroundRemoval, MockupNews



@admin.register(AIImageGeneration)
class AIImageGenerationAdmin(admin.ModelAdmin):
    list_display = ('description', 'generated_image', 'created_at')
    search_fields = ('description',)

@admin.register(IconGeneration)
class IconGenerationAdmin(admin.ModelAdmin):
    list_display = ('icon_description', 'generated_icon', 'created_at')
    search_fields = ('icon_description',)

@admin.register(PDFGeneration)
class PDFGenerationAdmin(admin.ModelAdmin):
    list_display = ('content', 'generated_pdf', 'created_at')
    search_fields = ('content',)

@admin.register(VideoGeneration)
class VideoGenerationAdmin(admin.ModelAdmin):
    list_display = ('video_content', 'generated_video', 'created_at')
    search_fields = ('video_content',)

@admin.register(BackgroundGeneration)
class BackgroundGenerationAdmin(admin.ModelAdmin):
    list_display = ('bg_description', 'generated_background', 'created_at')
    search_fields = ('bg_description',)

@admin.register(BackgroundRemoval)
class BackgroundRemovalAdmin(admin.ModelAdmin):
    list_display = ('original_image', 'removed_bg_image', 'created_at')
    search_fields = ('original_image',)

@admin.register(MockupNews)
class MockupNewsAdmin(admin.ModelAdmin):
    list_display = ('headline', 'body', 'generated_mockup', 'created_at')
    search_fields = ('headline', 'body')


    