from django.urls import path

from .views import home_page_view,AboutPageView

urlpatterns = [
    # To prevent errors if file names are changed 
     path("about/", AboutPageView.as_view(), name="about"), 
    path("", home_page_view, name="home"), 
]