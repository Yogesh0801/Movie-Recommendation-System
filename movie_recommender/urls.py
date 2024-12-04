"""movie_recommender URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# movie_recommender/urls.py
from django.contrib import admin
from django.urls import path
from recommendations import views
from recommendations import views as remoteuser
from movie_recommender import settings
from service_provider import views as serviceprovider
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name="index"),
    path('login', views.login, name="login"),
    path('Register1/', views.Register1, name="Register1"),
    #path(r'ViewYourProfile/', views.ViewYourProfile, name="ViewYourProfile"),
    path('recommend/', views.recommend, name='recommend'),
    # path(r'^Search_DataSets/$', views.Search_DataSets, name="Search_DataSets"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

