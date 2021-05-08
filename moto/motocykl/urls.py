from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('list', views.MotoListView.as_view(), name='list'),
    path('detail/<int:pk>', views.MotoDetailView.as_view(), name='detail'),
]