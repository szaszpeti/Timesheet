from django.urls import path

from .views import HomeView, EntryView, CreateEntryView, StartView

urlpatterns = [
    path('', StartView.as_view(), name = 'welcome'),
    path('list/', HomeView.as_view(), name = 'blog-home'),
    path('entry/<int:pk>/', EntryView.as_view(), name = 'entry-detail'),
    path('create_entry/', CreateEntryView.as_view(success_url='/'), name = 'entry-create')
    
    
    
]# -*- coding: utf-8 -*-

