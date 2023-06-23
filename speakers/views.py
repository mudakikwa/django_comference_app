from django.shortcuts import render, get_object_or_404
from .models import Speaker

def create_speaker(request):
    # Implement the logic to create a new speaker profile
    pass

def update_speaker(request, speaker_id):
    # Implement the logic to update an existing speaker profile
    pass

def delete_speaker(request, speaker_id):
    # Implement the logic to delete a speaker profile
    pass

def speaker_details(request, speaker_id):
    speaker = get_object_or_404(Speaker, id=speaker_id)
    context = {'speaker': speaker}
    return render(request, 'speakers/details.html', context)

def speaker_list(request):
    speakers = Speaker.objects.all()
    context = {'speakers': speakers}
    return render(request, 'speakers/list.html', context)
