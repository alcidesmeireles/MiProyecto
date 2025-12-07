from django.urls import path
from . import views

urlpatterns = [
    path('', views.MarcaListView.as_view(), name='marca_list'),
    path('crear/', views.MarcaCreateView.as_view(), name='marca_create'),
    path('<int:pk>/editar/', views.MarcaUpdateView.as_view(), name='marca_update'),
    path('<int:pk>/eliminar/', views.MarcaDeleteView.as_view(), name='marca_delete'),
]
