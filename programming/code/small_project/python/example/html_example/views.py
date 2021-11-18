import time

from django.http import StreamingHttpResponse
from django.shortcuts import render
from django.utils.timezone import now

def web_workers(request):
    return render(request, 'web_workers.html')

def server_sent_events(request):
    return render(request, 'server_sent_events.html')

def eventsource(request):
    response = StreamingHttpResponse(stream_generator(), content_type='text/event-stream')
    response['Cache-Control'] = 'no-cache'
    return response

def stream_generator():
    while True:
        yield u'data: The server time is: {}\n\n'.format(str(now()))
        time.sleep(2)

def chat(request):
    return render(request, 'chat.html')

def chat_room(request, room_name):
    # print(room_name)
    # return render(request, 'chat_room.html', {
    #     'room_name': room_name
    # })
    return render(request, 'chat_room.html', {
        'room_name': room_name
    })
