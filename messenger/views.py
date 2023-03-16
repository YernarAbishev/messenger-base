from django.shortcuts import render, get_object_or_404
from .models import Chat, Message

def chat_list(request):
    chats = Chat.objects.filter(members=request.user)
    context = {'chats': chats}
    return render(request, 'chat_list.html', context)

def chat_detail(request, pk):
    chat = get_object_or_404(Chat, pk=pk)
    messages = Message.objects.all()
    return render(request, "chat_detail.html", {
        'chat': chat,
        'messages': messages
    })