from django.shortcuts import render, get_object_or_404

from notes.models import Note, Category

def index(request):
    latest_note_list = Note.objects.all().order_by('-pub_date')[:5]
    category_list = Category.objects.all().order_by('name')
    context = {'latest_note_list': latest_note_list, 'category_list': category_list}
    return render(request, 'notes/index.html', context)

def detail(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    return render(request, 'notes/detail.html', {'note': note})
