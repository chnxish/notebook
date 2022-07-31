from django.urls import path
from . import views

urlpatterns = {
    path('web_workers', views.web_workers),
    path('server_sent_events', views.server_sent_events),
    path('eventsource', views.eventsource),
    path('chat', views.chat),
    path('<str:room_name>/', views.chat_room),
}
