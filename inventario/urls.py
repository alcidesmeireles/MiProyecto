from django.urls import path
from . import views
from .views import RepuestoListView, RepuestoDetailView, RepuestoCreateView, RepuestoUpdateView, RepuestoDeleteView

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('about/', views.about, name='about'),  
    # marcas y clientes
    path('agregar-marca/', views.agregar_marca, name='agregar_marca'),
    # CRUD repuestos (CBV)
    path('repuestos/', RepuestoListView.as_view(), name='repuesto_list'),
    path('repuestos/crear/', RepuestoCreateView.as_view(), name='repuesto_create'),
    path('repuestos/<int:pk>/', RepuestoDetailView.as_view(), name='repuesto_detail'),
    path('repuestos/<int:pk>/editar/', RepuestoUpdateView.as_view(), name='repuesto_update'),
    path('repuestos/<int:pk>/borrar/', RepuestoDeleteView.as_view(), name='repuesto_delete'),
    path('buscar-repuesto/', views.buscar_repuesto, name='buscar_repuesto'),
]
