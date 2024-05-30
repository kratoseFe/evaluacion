from django.shortcuts import render
from quiz.models import Estudianate
# Create your views here.

def tabla(request):
    estudiantes = Estudianate.objects.all()
    return render(request, 'tabla.html', {'estu': estudiantes})