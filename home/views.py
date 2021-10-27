from django.shortcuts import render, redirect
from .models import Movie
from .forms import MoiveForm


def home(request):
    movies = Movie.objects.all()
    context = {'movies': movies}
    return render(request, 'home/home.html', context)


def sort(request, slug):
    movies = Movie.objects.all().order_by(slug)

    context = {'movies': movies}
    return render(request, 'home/home.html', context)


def detail(request, id):
    detail = Movie.objects.get(id=id)
    context = {'detail': detail}
    return render(request, 'home/detail.html', context)


def play(request, id):
    movie = Movie.objects.get(id=id)
    movie.watch_count += 1
    movie.save()
    return redirect('https://www.netflix.com/in/')


def create(request):
    form = MoiveForm()

    if request.method == 'POST':
        form = MoiveForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'home/form.html', context)


def update(request, id):
    movie = Movie.objects.get(id=id)
    form = MoiveForm(instance=movie)

    if request.method == 'POST':
        form = MoiveForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'home/form.html', context)


def delete(request, id):
    movie = Movie.objects.get(id=id)
    movie.delete()
    return redirect('home')
