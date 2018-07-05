
# THESE ARE THE URL FORN THE APPLICACIONT HELLO
#as oppose to the urls.py file declare in the gettingstarted folder, which is the root od the proyect

from django.urls import path

# . is the current directory
from . import views

#now, url for each view
urlpatterns = [
    # path asociated to a function inside the view
    path("", views.index, name='index' ),
    #path("detail/<int:id>/", views.detail, name='detail' ),
    path("map/", views.map, name='map' ),
    path("submit/", views.submit, name='submit' )
    # 3rd parameter : name='path_name'
    # then, in the html file use tag
    # <a hrf="{% url 'path_name' %}"> Go to path name </a>
    # if there where params like an id :
    # <a hrf="{% url 'path_name' id %}"> Go to path name </a>
]
