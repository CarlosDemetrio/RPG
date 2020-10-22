from django.urls import path

from Ficha import views

urlpatterns = [
    path('', views.ficha_list, name='ficha_lista'),
    path('ficha/<id>', views.ficha_detail, name='post_detail'),
]
