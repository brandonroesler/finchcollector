from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('birds/', views.birds_index, name='index'),
    path('birds/<int:bird_id>/', views.birds_detail, name='detail'),
    path('birds/create/', views.BirdCreate.as_view(), name='birds_create'),
    path('birds/<int:pk>/update', views.BirdUpdate.as_view(), name='birds_update'),
    path('birds/<int:pk>/delete', views.BirdDelete.as_view(), name='birds_delete'),
    path('birds/<int:bird_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    path('birds/<int:bird_id>/assoc_language/<int:language_id>/', views.assoc_language, name='assoc_language'),
    path('birds/<int:bird_id>/unassoc_language/<int:language_id>/', views.unassoc_language, name='unassoc_language'),
    path('languages/', views.LanguageList.as_view(), name='languages_index'),
    path('languages/<int:pk>/', views.LanguageDetail.as_view(), name='languages_detail'),
    path('languages/create/', views.LanguageCreate.as_view(), name='languages_create'),
    path('languages/<int:pk>/update/', views.LanguageUpdate.as_view(), name='languages_update'),
    path('languages/<int:pk>/delete/', views.LanguageDelete.as_view(), name='languages_delete'),    
    path('birds/<int:bird_id>/add_photo/', views.add_photo, name='add_photo'),
]