from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.utils.crypto import get_random_string
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from ..mixins import AdminDashBoardMixin

User = get_user_model()


# get list of all trainers
class TrainerListTemplateView(AdminDashBoardMixin, ListView):
    model = User
    template_name = "dashboard/trainers/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["trainers"] = User.objects.filter(
            role="Trainer").order_by("-id")
        return context


class TrainerDetailTemplateView(AdminDashBoardMixin, DetailView):
    model = User
    template_name = "dashboard/trainers/details.html"
    context_object_name = 'trainer'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[
            "personal_trainings"] = self.object.trainer_personal_trainings.all(
            )
        context["gym_classes"] = self.object.classes_in_charge.all()
        context['trainer_profile'] = self.object.trainer_profiles
        return context


class TrainerRegistrationTemplateView(AdminDashBoardMixin, CreateView):
    model = User
    fields = [
        'first_name',
        'last_name',
        'email',
        'phone_number',
        'location',
        'image',
    ]
    template_name = "dashboard/members/add.html"

    def form_valid(self, form):

        user = form.save(commit=False)
        user.username = user.email
        default_password = get_random_string(7)

        user.set_password(default_password)
        user.role = "Trainer"

        user.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("dashboard:trainers_dashboard:trainer_details",
                            kwargs={"pk": self.object.pk})


# class customer edit form
class TrainerEditTemplateView(AdminDashBoardMixin, UpdateView):
    model = User
    fields = [
        'first_name',
        'last_name',
        'email',
        'phone_number',
        'location',
        'image',
    ]
    template_name = "dashboard/members/add.html"

    def get_success_url(self):
        return reverse_lazy("dashboard:trainers_dashboard:trainer_details",
                            kwargs={"pk": self.object.pk})
