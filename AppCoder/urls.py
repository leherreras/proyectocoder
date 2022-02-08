from django.urls import path
from AppCoder.views import *


urlpatterns = [
    path('curso/list', CursoList.as_view(), name='List'),
    path('<int:pk>/', CursoDetalle.as_view(), name='Detail'),
    path('nuevo/', CursoCreacion.as_view(), name='New'),
    path('editar/<int:pk>/', CursoUpdate.as_view(), name='Edit'),
    path('borrar/<int:pk>/', CursoDelete.as_view(), name='Delete'),
]
