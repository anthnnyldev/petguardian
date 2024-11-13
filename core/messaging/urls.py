from django.urls import path
from .views import send_message, inbox, message_detail

app_name = 'messaging'

urlpatterns = [
    path('send_message/<int:user_id>/', send_message, name='send_message'),
    path('message/<int:sender_id>/', message_detail, name='message_detail'),  # Cambiado a sender_id
    path('inbox/', inbox, name='inbox'),
]