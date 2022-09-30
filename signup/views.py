from django.shortcuts import redirect

# Create your views here.


def index_view(request):
    return redirect('admin/')
