from django.shortcuts import render

from .models import (
    CassandraMessage,
)


def index(request):
    return render(request, 'chat/index.html')

def room(request, room_name):
    username = request.GET.get('username', 'Anonymous')
    messages = CassandraMessage.objects.filter(room=room_name)[:25]

    return render(request, 'chat/room.html', {'room_name': room_name, 'username': username, 'messages': messages})
