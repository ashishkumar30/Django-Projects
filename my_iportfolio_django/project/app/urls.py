from django.conf.urls import include,url
from django.contrib import admin
from . import views
from django.contrib import admin
from django.urls import path
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static


from django.conf.urls import url
from . import views

from django.conf.urls import url

from django.conf.urls import url

from . import views
from django.conf.urls import include,url
from django.contrib import admin
from django.contrib import admin
from django.urls import path
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home ),
    path('create',views.create, name='submit data'),
    path('uploadresume/', views.uploadresume ),  # going to upload resume
    path('templateresume/', views.templateresumeopen ), # going to template
    path('templateresume/gotohome/', views.tohome ),
    path('templateresume/creates/', views.createresume), # wehen cooming from template to create model

    path('creates/create/', views.create ), ## storin data
    path('templateresume/creates/create/', views.create ), # storing data from templates
    path('templateresume/uploadresu/', views.uploadresume),



]

#method="GET"
