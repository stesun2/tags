from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.shortcuts import render
from .forms import TagForm
from tags.models import Tag  # The DB model
from IPython import embed

class HomePageView(FormView):
    # Used to render the page on initial get of '/' route.
    template_name = 'home.html' # Can do this because FormView inherits TemplateResponseMixin

    def index(request):
        tags = Tag.objects.all()
        return render(request, 'home.html', {'form': TagForm(), 'tags': tags})

    # What prompts Django to call this method?
    # urls.py associates it with the '/tags/' route.  Except that it's also called
    # from the '' route ... !!?
    def tags(request):
        #embed()
        if request.method=='POST':
            form = TagForm(request.POST)
            t = Tag(name=request.POST['tag'])
            t.save()
            return HttpResponseRedirect('/')
        else:
            form = TagForm()
            return render(request, 'home.html', {'form': form, 'tags': tags})

    # 'name' corresponds to and is populated by the <name> param in urls.py
    def tag(request, name):
        tag = Tag.objects.get(name=name)
        tag.delete()
        return HttpResponseRedirect('/')

class AboutPageView(TemplateView):
    template_name = 'about.html'
