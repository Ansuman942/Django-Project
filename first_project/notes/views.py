from django.shortcuts import get_object_or_404, redirect
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Note
from .forms import NoteForm

class NoteListView(LoginRequiredMixin, ListView):
    model = Note
    template_name = "notes/note_list.html"
    context_object_name = "notes"

    def get_queryset(self):
        return Note.objects.filter(author=self.request.user)

class NoteDetailView(LoginRequiredMixin, DetailView):
    model = Note
    template_name = "notes/note_detail.html"
    context_object_name = "note"

    def get_object(self, queryset=None):
        return get_object_or_404(Note, pk=self.kwargs["pk"], author=self.request.user)

class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    form_class = NoteForm
    template_name = "notes/note_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user  
        return super().form_valid(form)

    def get_success_url(self):
        return redirect("note_list")

class NoteUpdateView(LoginRequiredMixin, UpdateView):
    model = Note
    form_class = NoteForm
    template_name = "notes/note_form.html"

    def get_object(self, queryset=None):
        note = super().get_object(queryset)
        if note.author != self.request.user:
            raise PermissionDenied  
        return note

    def get_success_url(self):
        return redirect("note_detail", pk=self.object.pk)

class NoteDeleteView(LoginRequiredMixin, DeleteView):
    model = Note
    template_name = "notes/note_confirm_delete.html"

    def get_object(self, queryset=None):
        note = super().get_object(queryset)
        if note.author != self.request.user:
            raise PermissionDenied  
        return note

    def get_success_url(self):
        return redirect("note_list")