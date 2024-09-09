from django.urls import path
from .views import NoteListView, NoteDetailView, NoteCreateView, NoteUpdateView, NoteDeleteView

urlpatterns = [
    path("", NoteListView.as_view(), name="note_list"),
    path("<int:pk>/", NoteDetailView.as_view(), name="note_detail"),
    path("create/", NoteCreateView.as_view(), name="note_create"),
    path("<int:pk>/edit/", NoteUpdateView.as_view(), name="note_update"),
    path("<int:pk>/delete/", NoteDeleteView.as_view(), name="note_delete"),
]