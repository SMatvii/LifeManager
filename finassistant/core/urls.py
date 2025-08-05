from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("profile/", views.profile, name="profile"),
    path("events/", views.events, name="events"),
    path("events/add/", views.add_event, name="add_event"),
    path("events/toggle/<int:event_id>/", views.toggle_event, name="toggle_event"),
    path("transactions/", views.transactions, name="transactions"),
    path("transactions/add/<str:type>/", views.add_transaction, name="add_transaction"),
    # path('profile/', views.profile_view, name='profile'),
    # path('profile/edit/', views.profile_edit, name='profile_edit'),
    # path('profile/username/', views.change_username, name='change_username'),
]