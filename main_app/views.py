from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Game, Bar

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def games_index(request):
    games = Game.objects.all()
    return render(request, 'games/index.html', {'games': games})


#@login_required
#Add to create function to attach to certain user
# def form_valid(self, form):
    # form.instance.user = self.request.user 
    # return super().form_valid(form)

def bars_index(request):
  bars = Bar.objects.all()
  return render(request, 'bars/bar_index.html', {'bars': bars})


def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('/')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

def add_game(request, bar_id):
  form = BarForm(request.POST)
  if form.is_valid():
    new_game = game.save(commit=False)
    new_game.bar_id = bar_id
    new_game.save()
  return redirect('detail', game_id=game_id)

class BarCreate(LoginRequiredMixin, CreateView):
  model = Bar
  fields = ['name', 'location', 'price_range', 'has_food']
  success_url = '/bars/'
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

def bar_details(request, bar_id):
  bar = Bar.objects.get(id=bar_id)
  return render(request, 'bars/bar_details.html', {'bar': bar})