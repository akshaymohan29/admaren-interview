from django.urls import path
from .views import CreateView,SnippetOverviewView,DetailView,UpdateView,DeleteView,TagListView,TagDetailView

urlpatterns = [
   path('create',CreateView.as_view(),name='create'),
   path('snippets', SnippetOverviewView.as_view()),
   path('details/<int:id>', DetailView.as_view(), name='detail'),
   path('update/<int:id>', UpdateView.as_view(), name='update'),
   path('delete/<int:id>', DeleteView.as_view(), name='delete'),
   path('tags/', TagListView.as_view(), name='tag-list'),
   path('tags-details/<int:id>', TagDetailView.as_view(), name='tag-detail'),
   
]