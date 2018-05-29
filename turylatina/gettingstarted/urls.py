from django.conf.urls import include, url
from django.urls import include, path

from django.contrib import admin
admin.autodiscover()

import hello.views

# THIS ARE THE URL FOR THE PRYECT AS A HOLE

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    path('', include('hello.urls')),
    #url(r'^$', hello.views.index, name='index'),
    #url(r'^db', hello.views.db, name='db'),
    path('admin/', admin.site.urls)
]
