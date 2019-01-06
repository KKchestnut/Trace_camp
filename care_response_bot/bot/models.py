from django.db import models
from django.urls import reverse_lazy
# Create your models here.


class BotResponse(models.Model):
    responses = models.TextField()
    name = models.CharField(max_length=70, default='')
    answer = models.TextField(default='')

    class Meta():
        pass

    def __str__(self):
        return f'{self.responses}, {self.name}'

    def get_absolute_url(self):
        return reverse_lazy('bot_comment_detail', args=[str(self.id)])
