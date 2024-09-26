from django.shortcuts import render, redirect
from .models import AIImageGeneration, IconGeneration, PDFGeneration, VideoGeneration, BackgroundGeneration, BackgroundRemoval, MockupNews
from .forms import AIImageGenerationForm, IconGenerationForm, PDFGenerationForm, VideoGenerationForm, BackgroundGenerationForm, BackgroundRemovalForm, MockupNewsForm

# AI Image Generation View
def ai_image_generation_view(request):
    if request.method == 'POST':
        form = AIImageGenerationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Save the form data (image + description)
            return redirect('ai-image-generation')  # Redirect to avoid re-submitting the form
    else:
        form = AIImageGenerationForm()

    # Retrieve all images to display them in the card layout
    images = AIImageGeneration.objects.all()

    return render(request, 'ai_image_generation.html', {'form': form, 'images': images})

# Icon Generation View
def icon_generation_view(request):
    if request.method == 'POST':
        form = IconGenerationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('icon-generation')
    else:
        form = IconGenerationForm()
    return render(request, 'icon_generation.html', {'form': form})

# PDF Generation View
def pdf_generation_view(request):
    if request.method == 'POST':
        form = PDFGenerationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pdf-generation')
    else:
        form = PDFGenerationForm()
    return render(request, 'pdf_generation.html', {'form': form})

# Video Generation View
def video_generation_view(request):
    if request.method == 'POST':
        form = VideoGenerationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('video-generation')
    else:
        form = VideoGenerationForm()
    return render(request, 'video_generation.html', {'form': form})

# Background Generation View
def background_generation_view(request):
    if request.method == 'POST':
        form = BackgroundGenerationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('background-generation')
    else:
        form = BackgroundGenerationForm()
    return render(request, 'background_generation.html', {'form': form})

# Background Removal View
def background_removal_view(request):
    if request.method == 'POST':
        form = BackgroundRemovalForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('background-removal')
    else:
        form = BackgroundRemovalForm()
    return render(request, 'background_removal.html', {'form': form})

# Mockup News View
def mockup_news_view(request):
    if request.method == 'POST':
        form = MockupNewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('mockup-news')
    else:
        form = MockupNewsForm()
    return render(request, 'mockup_news.html', {'form': form})
