import uuid
import boto3
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Game, Bar, Photo

S3_BASE_URL = 'https://s3-us-east-2.amazonaws.com/'
BUCKET = 'thebestestbarcadeapp'
# Create your views here.

@login_required
def add_photo(request, game_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            photo = Photo(url=url, game_id=game_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('game_details', game_id=game_id)

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


def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def game_details(request, game_id):
  game = Game.objects.get(id=game_id)
  return render(request, 'games/detail.html', {'game': game})

def games_index(request):
  games = Game.objects.all()
  return render(request, 'games/index.html', {'games': games})

def bars_index(request):
  bars = Bar.objects.all()
  return render(request, 'bars/bar_index.html', {'bars': bars})

def bar_details(request, bar_id):
  games = Game.objects.all()
  bar = Bar.objects.get(id=bar_id)
  return render(request, 'bars/bar_details.html', {'bar': bar, 'games': games, 'user' : request.user})

class GameCreate(LoginRequiredMixin, CreateView):
  model = Game
  fields = ['name', 'price', 'number_of_players', 'condition', 'comments']
  success_url = '/games/'
  def form_valid(self, form):
    form.instance.user = self.request.user
    # url params are available as a kwarg on self as follows
    form.instance.bar_id = self.kwargs['bar_id']
    return super().form_valid(form)

class GameDelete(LoginRequiredMixin, DeleteView):
  model = Game
  success_url = '/games/'

class GameUpdate(LoginRequiredMixin, UpdateView):
  model = Game
  fields = '__all__'

class BarCreate(LoginRequiredMixin, CreateView):
  model = Bar
  fields = ['name', 'location', 'price_range', 'has_food']
  success_url = '/bars/'
  def form_valid(self, form):
    form.instance.user = self.request.user
    print("form here: ")
    print(form.instance.has_food)
    return super().form_valid(form)

class BarDelete(LoginRequiredMixin, DeleteView):
  model = Bar
  success_url = '/bars/'

class BarUpdate(LoginRequiredMixin, UpdateView):
  model = Bar
  fields = ['name', 'location', 'price_range', 'has_food']


