from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from batteries.models import Battery
from batteries.forms import BatteryForm
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


@method_decorator(login_required, name='dispatch')
class BatteryCreate(CreateView):
    model = Battery
    fields = ['cells', 'capacity', 'nickname', 'barcode', 'cell_voltage']

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(BatteryCreate, self).get_context_data(**kwargs)
        context['task'] = 'Create'
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(BatteryCreate, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class BatteryUpdate(UpdateView):
    model = Battery
    fields = ['cells', 'capacity', 'nickname', 'barcode', 'cell_voltage']

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(BatteryUpdate, self).get_context_data(**kwargs)
        context['task'] = 'Update'
        return context


@method_decorator(login_required, name='dispatch')
class BatteryDetail(DetailView):

    model = Battery

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(BatteryDetail, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        # context['battery_list'] = Battery.objects.all()
        return context


@method_decorator(login_required, name='dispatch')
class BatteryListView(ListView):

    def get_queryset(self):
        return Battery.objects.filter(user=self.request.user)


# Create your views here.
def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password1')
            )
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


@login_required
def view_batteries(request):
    user = request.user
    batteries = Battery.objects.filter(user=user)
    return render(request, 'batteries/battery_list.html', {'batteries': batteries})


@login_required
def battery_detail(request, battery=None):
    if battery is None:
        form = BatteryForm(data=request.POST)
        if request.method == 'POST':
            if form.is_valid():
                form.save(for_user=user)
                return redirect('batteries')
        else:
            return render(request, 'batteries/battery_detail.html', {'form': form})