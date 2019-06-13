from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Bird, Language, Photo
from .forms import FeedingForm
S3_BASE_URL = 'https://s3-us-east-2.amazonaws.com/'
BUCKET = 'catcollector2683'
import uuid
import boto3

# Create your views here.
class BirdCreate(CreateView):
    model = Bird
    fields = ['name', 'breed', 'description', 'age' ]
    success_url = '/birds/'

class BirdUpdate(UpdateView):
    model = Bird
    fields = ['breed', 'description', 'age']

class BirdDelete(DeleteView):
    model = Bird
    success_url = '/birds/'

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def birds_index(request):
    birds = Bird.objects.all()
    return render(request, 'birds/index.html', { 'birds': birds })

def birds_detail(request, bird_id):
    bird = Bird.objects.get(id=bird_id)
    languages_bird_doesnt_have = Language.objects.exclude(id__in=bird.languages.all().values_list('id'))
    feeding_form = FeedingForm()
    return render(request, 'birds/detail.html', {
        'bird': bird, 'languages': languages_bird_doesnt_have, 'feeding_form': feeding_form
    })

def add_feeding(request, bird_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
      new_feeding = form.save(commit=False)
      new_feeding.bird_id = bird_id
      new_feeding.save()
  return redirect('detail', bird_id=bird_id)

class LanguageList(ListView):
  model = Language

class LanguageDetail(DetailView):
  model = Language

class LanguageCreate(CreateView):
  model = Language
  fields = '__all__'

class LanguageUpdate(UpdateView):
  model = Language
  fields = '__all__'

class LanguageDelete(DeleteView):
  model = Language
  success_url = '/languages/'

def assoc_language(request, bird_id, language_id):
  Bird.objects.get(id=bird_id).languages.add(language_id)
  return redirect('detail', bird_id=bird_id)

def unassoc_language(request, bird_id, language_id):
  Bird.objects.get(id=bird_id).languages.remove(language_id)
  return redirect('detail', bird_id=bird_id)

def add_photo(request, bird_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      photo = Photo(url=url, bird_id=bird_id)
      photo.save()
    except:
      print('An error occurred uploading file to S3')
  return redirect('detail', bird_id=bird_id)