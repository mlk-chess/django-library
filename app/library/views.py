from django.shortcuts import render, get_object_or_404
from .models import Library


def library_list(request):
    libraries = Library.objects.all()
    return render(request, 'library/index.html', {'libraries': libraries})


def library_detail(request, library_id):
    library = Library.objects.get(id=1)
    return render(request, 'library/library_detail.html', {'library': library})
