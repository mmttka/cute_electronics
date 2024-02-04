from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView,
    )
from .models import Creation, Review
from .forms import CreationForm
from django.urls import reverse,reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Avg

class CreationsListView(ListView):
    template_name = "my_creations/creations_list.html"
    model = Creation
    queryset = Creation.objects.all().order_by('-created_at')
    paginate_by = 10

class CreationDetailView(DetailView):
    template_name = "my_creations/creation_detail.html"
    model = Creation

class CreationCreateView(LoginRequiredMixin, CreateView):
    model = Creation
    form_class = CreationForm
    template_name = "my_creations/creation_create.html"
    success_url = reverse_lazy("my_creations:creations-list")

    def form_valid(self, form):
        form.instance.user = self.request.user

        return super().form_valid(form)

class CreationDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "my_creations/creation_delete.html"
    model = Creation
    success_url = reverse_lazy("my_creations:creations-list")



class CreationUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "my_creations/creation_update.html"
    model = Creation
    form_class = CreationForm
    # success_url = reverse_lazy("my_creations:creations-list")

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)

        if obj.user != self.request.user:
            raise PermissionDenied

        return obj

    def get_success_url(self):
        return reverse("my_creations:creation-detail", kwargs={'pk': self.object.id})


def index_view(request):
    object_list = Creation.objects.order_by("-created_at")[:6]
    ranking_list = Creation.objects.annotate(avg_rating=Avg('review__rate')).order_by('-avg_rating')[:6]
    return render(request,
                  "my_creations/index.html",
                  {"object_list": object_list, "ranking_list": ranking_list})


class CreationReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    fields = ("creation", "title", "text", "rate")
    template_name = "my_creations/creation_review_create.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["creation"] = Creation.objects.get(pk=self.kwargs["creation_id"])
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("my_creations:creation-detail", kwargs={'pk': self.object.creation.id})






