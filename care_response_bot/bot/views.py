from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from bot.models import BotResponse
from django.http import HttpResponse
from bot.form.forms import BotResponseForm
from django.urls import reverse_lazy
import random
import requests

# Create your views here.


class BotResponseListView(ListView):
    model = BotResponse


class BotResponseDetailView(DetailView):
    model = BotResponse
    template_name = 'bot/botresponse_detail.html'

    def get_context_data(self, **kwargs):
        context = super(BotResponseDetailView, self).get_context_data(**kwargs)
        file = open("responses.txt", "r")
        #answer_file = file.readline(random.randint(1, 12))
        real_file = file.readlines()
        answer_file = real_file[random.randint(0,12)]
        context['answer'] = answer_file
        return context


class BotResponseCreateView(CreateView):
    form_class = BotResponseForm
    template_name = 'bot/botresponse_form.html'

    # def __init__(self):
    #     super().__init__()
    #     self.comment = ""
    #
    # def get(self, requests):
    #     r = requests.get(f'https://www.happier.com/blog/nice-things-to-say-100-compliments/')
    #     url = r.json()["url"]
    #     self.comment = url
    #     get_response = super().get(requests)
    #     return get_response


class BotResponseUpdateView(UpdateView):
    model = BotResponse
    field = ['name', 'responses', 'answer']


class BotResponseDeleteView(DeleteView):
    model = BotResponse
    success_url = reverse_lazy('bot_comment_list')
