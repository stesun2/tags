from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.shortcuts import render
from .forms import TagForm

class HomePageView(FormView):
    # Used to render the page on initial get of '/' route.
    template_name = 'home.html' # Can do this because FormView inherits TemplateResponseMixin

    # Draw the form on initial get of '/' route.
    form_class = TagForm

    # What prompts Django to call this method?
    # urls.py associates it with the '/tags/' route.  Except that it's also called
    # from the '' route ... !!?
    def tag(request):
        if request.method=='POST':
            form = TagForm(request.POST)
            print(request.POST['tag'])  # Here, would typically update something in a database
            return HttpResponseRedirect('/')
        else:
            form = TagForm()
        return render(request, 'home.html', {'form': form})

class AboutPageView(TemplateView):
    template_name = 'about.html'
