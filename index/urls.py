from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('index/', views.ProductList.as_view()),
    path('<int:id>.html', views.model_index),
]
