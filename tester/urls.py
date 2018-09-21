from django.urls import path
from tester import views

urlpatterns = [
    path('', views.index_resemblejs, name='index_resemblejs'),
    path('cypress_process', views.headless_resemblejs_process, name='process_resemblejs'),
]