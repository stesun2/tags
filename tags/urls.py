from django.urls import path
from .views import HomePageView, AboutPageView

urlpatterns = [
    # the name parameter is handy if you need to reference the url in code by that name
    path('', HomePageView.index, name='home'),
    path('tags/', HomePageView.tags, name='tags' ),
    path('about/', AboutPageView.as_view(), name='about'),
]
