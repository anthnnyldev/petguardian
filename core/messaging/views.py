from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from core.user.models import User
from .models import Message
from .forms import MessageForm, MessageReplyForm
from django.db.models import Q

@login_required
def send_message(request, user_id):
    recipient = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.recipient = recipient
            message.save()
            return redirect('user:dashboard')
    else:
        form = MessageForm(initial={'recipient': recipient})
    return render(request, 'send_message.html', {'form': form, 'recipient': recipient})

@login_required
def message_detail(request, sender_id):
    user = request.user
    sender = get_object_or_404(User, id=sender_id)
    messages = Message.objects.filter(
        (Q(sender=sender) & Q(recipient=user)) | (Q(sender=user) & Q(recipient=sender))
    ).order_by('timestamp')

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.sender = user
            reply.recipient = sender
            reply.save()
            return redirect('messaging:message_detail', sender_id=sender.id)
    else:
        form = MessageForm()

    return render(request, 'message_detail.html', {'sender': sender, 'messages': messages, 'form': form})

@login_required
def inbox(request):
    # Obtener todos los mensajes recibidos por el usuario
    messages = Message.objects.filter(recipient=request.user).order_by('-timestamp')
    
    # Contar mensajes no leídos
    unread_message_count = messages.filter(read=False).count()
    
    # Diccionario para almacenar el último mensaje por cada remitente
    unique_messages = {}
    
    for message in messages:
        # Usar el ID del remitente como clave para el diccionario
        sender_id = message.sender.id
        if sender_id not in unique_messages:
            unique_messages[sender_id] = message
    
    # Convertir el diccionario de mensajes únicos de nuevo a una lista
    unique_message_list = list(unique_messages.values())

    context = {
        'messages': unique_message_list,
        'unread_message_count': unread_message_count,
    }

    return render(request, 'inbox.html', context)