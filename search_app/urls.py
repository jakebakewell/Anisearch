from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('logout', views.logout),
    path('process_search', views.process_search),
    path('process_update', views.process_update),
    path('search_results', views.search_results),
    path('my_account', views.my_account),
    path('remove', views.remove),
]