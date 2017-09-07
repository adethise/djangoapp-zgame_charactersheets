from django.shortcuts import render, redirect, get_object_or_404

from .models import Character
from .forms import CharacterForm


def index(request):
    characters = Character.objects.all()
    return render(request, 'zgame_charactersheets/index.html',
            {'characters': characters})

def create(request):
    if request.method == 'POST':
        form = CharacterForm(request.POST)
        if form.is_valid():
            redirect(form.save())
    else:
        form = CharacterForm()

    return render(request, 'zgame_charactersheets/create.html',
            {'form': form})

def view(request, character_id):
    character = get_object_or_404(Character, pk=character_id)

    return render(request, 'zgame_charactersheets/view.html',
            {'character': character})
