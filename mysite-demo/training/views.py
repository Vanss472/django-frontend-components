from django.shortcuts import render

# Create your views here.

def training_index(request):
  return render(request, 'training-index.html')