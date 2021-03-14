from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Entry


class StartView(LoginRequiredMixin, TemplateView):
    template_name = 'entries/welcome.html'

class HomeView(LoginRequiredMixin, ListView):
    model = Entry
    template_name = 'entries/index.html'
    context_object_name = "timesheet_entries"
    ordering = ['-entry_date']
    paginate_by = 3
    
class EntryView(LoginRequiredMixin, DetailView):
    model = Entry
    template_name = 'entries/detail_entry.html'
    
    
class CreateEntryView(LoginRequiredMixin, CreateView):
    model = Entry
    template_name = 'entries/create_entry.html'
    fields = '__all__'
    
    
    #author is the user
    def form_valid(self,form):
        form.instance.entry_author = self.request.user
        return super().form_valid(form)