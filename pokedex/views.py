from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import login_required
from .models import Pokemon
from pokedex.forms import PokemonFrom
from django.shortcuts import redirect, render
def index(request):
    pokemons = Pokemon.objects.order_by('type') #se conoce como orm este enlace a base de datos
    template = loader.get_template('index.html')
    return HttpResponse(template.render({'pokemons': pokemons}, request))

def pokemon(request, pokemon_id):
    pokemon = Pokemon.objects.get(pk = pokemon_id)
    template = loader.get_template('display_pokemon.html')
    context = {
        'pokemon': pokemon
    }
    return HttpResponse(template.render(context, request))

@login_required




def add_pokemon(request):
    if request.method == 'POST':
        form = PokemonFrom(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')
        
    else:
        form = PokemonFrom()
        
    return render(request, 'add_pokemon.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'login.html'
    
    