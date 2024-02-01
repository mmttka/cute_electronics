from django.urls import path

from . import views

app_name = 'my_creations'
urlpatterns = [
    path('', views.index_view, name='index'),
    path('creations/', views.CreationsListView.as_view(), name="creations-list"),
    path('creations/<int:pk>/detail/', views.CreationDetailView.as_view(), name="creation-detail"),
    path('creations/create/', views.CreationCreateView.as_view(), name="creations-create"),
    path('creations/<int:pk>/delete/', views.CreationDeleteView.as_view(), name="creation-delete"),
    path('creations/<int:pk>/update/', views.CreationUpdateView.as_view(), name="creation-update"),
    path('creations/<int:creation_id>/review/', views.CreationReviewCreateView.as_view(), name="creation-review-create")
]


