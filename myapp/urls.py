
from django.urls import path
from myapp import views
from .views import  display_view
from .views import categorys
urlpatterns = [
    path('',views.index,name='index'),
    path('categorys/',categorys.as_view(),name='categorys'),
    path('display/', display_view, name='display'),
]
