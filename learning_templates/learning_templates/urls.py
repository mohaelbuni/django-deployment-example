from django.contrib import admin
from django.urls import path
from basic_app import views
from django.conf.urls import url , include




urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',views.index,name='index'),
    url(r'^basic_app/',include('basic_app.urls')),
  
]
