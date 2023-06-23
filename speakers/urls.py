from django.urls import path
from . import views

app_name = 'speakers'

urlpatterns = [
    path('create/', views.create_speaker, name='create'),
    path('update/<int:speaker_id>/', views.update_speaker, name='update'),
    path('delete/<int:speaker_id>/', views.delete_speaker, name='delete'),
    path('details/<int:speaker_id>/', views.speaker_details, name='details'),
    path('list/', views.speaker_list, name='list'),
]
