from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.views.decorators.csrf import csrf_protect
from django.utils.safestring import mark_safe
from .models import User, Taklif, FriendPhoto, StudentPhoto


import re

# --- Helper Functions ---

def clean_input(text):
    """Clean user input from HTML tags and limit length to prevent abuse."""
    cleaned = re.sub(r'<[^>]+>', '', text)  # Remove HTML tags
    return cleaned[:1000]  # Limit to 1000 characters

# --- Views ---

def kirish(request):
    """Simple view to render the login selection page."""
    return render(request, '1.html')

def akkauntbor(request):
    """Login view."""
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        name = request.POST.get('name', '').strip()

        try:
            user = User.objects.get(email=email)
            if user:
                messages.success(request, "Foydalanuvchi topildi!")
                return redirect('main')
        except User.DoesNotExist:
            messages.error(request, "Bu email bilan foydalanuvchi topilmadi.")
            return redirect('akkauntbor')

    return render(request, 'kirish.html')

def ruyxat(request):
    """User registration view."""

    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        dob = request.POST.get('dob')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Bu email manzil allaqachon ro'yxatdan o'tgan.")
            return redirect('register')
        else:
            User.objects.create(name=name, surname=surname, phone=phone, email=email, dob=dob)
            messages.success(request, "Ro'yxatdan o'tish muvaffaqiyatli amalga oshirildi!")
            return redirect('main')

    return render(request, 'register.html')

@csrf_protect
def resurslar(request):
    """Main resources view with translation and suggestion features."""
    input_text = ''
    translated_text = ''
    language_select = 'uzb'

    if request.method == 'POST':
        if 'taklif' in request.POST:
            fikr = request.POST.get('taklif', '').strip()
            if fikr:
                try:
                    cleaned_fikr = clean_input(fikr)
                    Taklif.objects.create(fikr=cleaned_fikr)
                    messages.success(request, "Taklifingiz muvaffaqiyatli yuborildi!")
                except ValidationError as e:
                    messages.error(request, f"Xato: {str(e)}")
                return redirect('resurslar')

        # Translation logic
        input_text = request.POST.get('inputText', '').strip()
        language_select = request.POST.get('languageSelect', 'uzb')


    return render(request, 'resurslar.html', {
        'input_text': input_text,
        'translated_text': mark_safe(translated_text),
        'language_select': language_select,
   
    })

def ustoz(request):
    photos = FriendPhoto.objects.all().order_by('-uploaded_at')
    return render(request, 'ustoz.html', {'photos': photos})

def uquv(request):
    photos = StudentPhoto.objects.all().order_by('-uploaded_at')
    return render(request, 'uquv.html', {'photos': photos})

def boglan(request):
    return render(request, 'boglan.html')

def main(request):
    return render(request, 'main.html')
