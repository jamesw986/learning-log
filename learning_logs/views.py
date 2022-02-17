from django.shortcuts import render

# Create your views here.
def index(request):
    """ THe home page for Learning Log """
    return render(request, 'learning_logs/index.html')