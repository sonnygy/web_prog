import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from .forms import CommentForm

class CommentConsumer(AsyncWebsocketConsumer):
    GROUP_NAME = 'comments'

    async def connect(self):
        await self.channel_layer.group_add(self.GROUP_NAME, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.GROUP_NAME, self.channel_name)

    async def receive(self, text_data):
        try:
            data = json.loads(text_data)
        except json.JSONDecodeError:
            await self.send(text_data=json.dumps({
                'type': 'error',
                'message': 'Неверный формат данных'
            }))
            return

        form_is_valid, comment_data, errors, debug = await self.process_form(data)

        if form_is_valid:
            await self.channel_layer.group_send(
                self.GROUP_NAME,
                {
                    'type': 'send_comment',
                    'comment': comment_data
                }
            )
        else:
            await self.send(text_data=json.dumps({
                'type': 'validation_error',
                'errors': errors
            }))

    async def send_comment(self, event):
        await self.send(text_data=json.dumps({
            'type': 'new_comment',
            'comment': event['comment']
        }))

    @sync_to_async
    def process_form(self, data):
        form = CommentForm(data=data)
        if form.is_valid():
            comment = form.save()
            return True, comment.to_json(), None, form.cleaned_data
        else:
            return False, None, form.errors.get_json_data(), form.errors


