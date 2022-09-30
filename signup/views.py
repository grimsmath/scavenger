from django.views.generic.base import RedirectView

# Create your views here.


class IndexView(RedirectView):
    url = '/admin/'
