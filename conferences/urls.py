from django.urls import path
from . import views

app_name = 'conferences'

urlpatterns = [
    path('create/', views.create_conference, name='create'),
    path('update/<int:conference_id>/', views.update_conference, name='update'),
    path('delete/<int:conference_id>/', views.delete_conference, name='delete'),
    path('details/<int:conference_id>/', views.conference_details, name='details'),
    path('list/', views.conference_list, name='list'),
]
