"""care_response_bot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from bot import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('care_response_bot/create/comment', views.BotResponseCreateView.as_view(), name="bot_comment_create"),
    path('care_response_bot/list', views.BotResponseListView.as_view(), name='bot_comment_list'),
    path('care_response_bot/detail/<int:pk>', views.BotResponseDetailView.as_view(), name="bot_comment_detail"),
    path('care_response_bot/delete/<int:pk>', views.BotResponseDeleteView.as_view()),
    path('care_response_bot/update/<int:pk>', views.BotResponseUpdateView.as_view()),
    ]
