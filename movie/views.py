from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Film, Acteur, Critique, Comment
from django.urls import reverse_lazy
from .forms import CritiqueForm, CommentForm
from django.db.models import Count


def home(request):
    return render(request, "movie/index.html")

class ListFilmView(ListView):   
    model = Film
    template_name = "movie/film_liste.html"
    context_object_name = "form" 

    def get_queryset(self):
        queryset = super().get_queryset()
        genre = self.request.GET.get('genre')
        annee = self.request.GET.get('date_sortie')
        note_min = self.request.GET.get('ntmoy')

        if genre:
            queryset = queryset.filter(genre=genre)
        if annee:
            queryset = queryset.filter(date_sortie__year=annee)
        if note_min:
            queryset = queryset.filter(ntmoy__gte=note_min)

        queryset = queryset.annotate(num_critics=Count('film')).order_by('-num_critics', '-ntmoy')

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genres'] = Film.choix_genre  
        return context


class DetailFilmView(DetailView):
    model = Film
    template_name = "movie/filmdetail.html"
    context_object_name = "film"


class CritqueCreateView(CreateView):
    model = Critique
    form_class = CritiqueForm
    template_name = "movie/critique.html"
    success_url = reverse_lazy("listfilm")

    def get_initial(self):
        initial = super().get_initial()
        initial["owner"] = self.request.user
        return initial

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class CommentCreateView(CreateView):
    model = Comment
    template_name = "movie/comment.html"
    form_class = CommentForm
    success_url = reverse_lazy("listfilm")

    def get_initial(self):
        initial = super().get_initial()
        initial["utilisateur"] = self.request.user
        return initial

    def form_valid(self, form):
        form.instance.utilisateur = self.request.user
        return super().form_valid(form)

class CommentListView(ListView):
    model = Comment
    template_name = "movie/commentlist.html"
    context_object_name = "comments"