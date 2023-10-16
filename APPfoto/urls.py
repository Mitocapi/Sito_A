from django.urls import path
from . import views

app_name = "APPfoto"

urlpatterns = [
    path(" /", views.home_view, name="home"),
    path("ricerca", views.search, name="cercaFoto"),
    path("ricerca/<str:sstring>/<str:where>", views.FotoListaRicercataView.as_view(), name="ricerca_risultati"),
    path("crea_foto/", views.CreateFotoView.as_view(), name="creafoto"),
    path("lista_foto/", views.FotoListView.as_view(), name="listafoto"),
    path("situation/", views.my_situation, name="situation"),
    path("acquisto/<int:foto_id>/", views.CreaAcquisto, name="acquisto"),
    path("fotografi_lista", views.FotografiListView.as_view(), name="listafotografi"),
    path('CreaRecensione/<int:acquisto_id>/', views.CreaRecensione, name='CreaRecensione'),
    path('recensioni_utente/', views.RecensioniUtente, name='RecensioniUtente'),
    path('for_you_page', views.forYouView, name="foryoupage")

]
