from django.contrib import admin
from django.urls import path, include

from core import views

# from core.views import ProfileListCreateView, ProfileDetailView, ProfileSubscribesListView

# urlpatterns = [
#     path('profile/', ProfileListCreateView.as_view(), name='profile'),
#     path('profile/<profile>/subscribes', ProfileSubscribesListView.as_view(), name='subscribers'),
#     path('all-profiles/', ProfileDetailView.as_view(), name='all-profiles'),
# ]

urlpatterns = [
    # path('profile/', ProfileListCreateView.as_view(), name='profile'),
    # path('profile/<profile>/subscribes', ProfileSubscribesListView.as_view(), name='subscribers'),
    path('all-profiles/', views.all_profiles, name='all-profiles'),
    path('profile/<profile_id>', views.profile, name='profile'),
]