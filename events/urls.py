from django.urls import path
from .views import EventListCreateView, EventRetrieveUpdateDestroyView, UpcomingEventListView, EventListByCategoryView

urlpatterns = [
    path('', EventListCreateView.as_view(), name='event_list_create'),
    path('<int:pk>/', EventRetrieveUpdateDestroyView.as_view(), name='event_detail'),
    path('upcoming/', UpcomingEventListView.as_view(), name='upcoming_events'),
    path('category/<str:category_name>/', EventListByCategoryView.as_view(), name='events_by_category'),
]
