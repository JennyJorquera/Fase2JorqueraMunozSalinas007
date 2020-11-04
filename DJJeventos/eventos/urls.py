from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('eventos/', views.eventos, name='eventos'),
    path('cotizacion/', views.cotizacion, name='cotizacion'),
    path('descEventos/', views.descEventos, name='descEventos'),
    path('reservas/', views.reservas, name='reservas'),
    path('listado/', views.ReservaListView.as_view(), name ='listado'),
    path('reserva/<int:pk>', views.ReservaDetailView.as_view(), name='reserva_detail')
]

urlpatterns += [
    path('reserva/create/', views.reservaCreate.as_view(), name='reserva_create'),
    path('reserva/<int:pk>/update/', views.reservaUpdate.as_view(), name='reserva_update'),
    path('reserva/delete/', views.reservaDelete.as_view(), name='reserva_delete'),
]

    