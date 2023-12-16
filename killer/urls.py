from django.urls import path 
from .views import killer , compo
urlpatterns = [
    path('',killer,name='killer'),
    path('aa',compo,name='compo')
    
]
