from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('test-firebase/', views.test_firebase, name='test_firebase'),
    path('usuarios/', views.lista_usuarios, name='lista_usuarios'),
    path('usuarios/nuevo/', views.crear_usuario, name='crear_usuario'),
    path('usuarios/editar/<str:user_id>/', views.editar_usuario, name='editar_usuario'),
    path('usuarios/eliminar/<str:user_id>/', views.eliminar_usuario, name='eliminar_usuario'),

]
