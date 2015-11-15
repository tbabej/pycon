from django.shortcuts import render

from django.views.generic.edit import CreateView, FormView

from .models import User

# Create your views here.
class UserCreateView(CreateView):
    model = User
    fields = ['username', 'password']
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(UserCreateView, self).get_context_data(**kwargs)
        context['users'] = User.objects.all()
        return context
