from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import Pokemon, Trainer
from .forms import PokemonForm, TrainerForm
from django.contrib.auth.views import LoginView



def index(request):
    #pokemons = Pokemon.objects.all() ## SELECT * FROM pokedex_pokemon
    pokemons = Pokemon.objects.order_by('type') ## SELECT * FROM pokedex_pokemon ORD
    template = loader.get_template('index.html')
    return HttpResponse(template.render({'pokemons': pokemons}, request))

def pokemon(request, pokemon_id):
    #SELECT * FROM pokedex_pokemon WHERE id='pokemon_id'
    pokemon = Pokemon.objects.get(id=pokemon_id)
    template = loader.get_template('display_pokemon.html')
    context = {
        'pokemon': pokemon
    }
    return HttpResponse(template.render(context, request))


@login_required
def add_pokemon(request):
    if request.method == 'POST':
        form = PokemonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')
    else:
        form = PokemonForm()
        
    return render(request, 'pokemon_form.html', {'form':form})

class CustomLoginView(LoginView):
    template_name='login.html'

@login_required
def edit_pokemon(request,id):
    pokemon=get_object_or_404(Pokemon,pk=id)
    if request.method == 'POST':
        form = PokemonForm(request.POST, request.FILES,instance=pokemon)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')
    else:
        form = PokemonForm(instance=pokemon)
        
    return render(request, 'pokemon_form.html',{'form':form})


@login_required
def delete_pokemon(request,id):
    pokemon=get_object_or_404(Pokemon,pk=id)
    pokemon.delete()
    return redirect("pokedex:index")
            

@login_required
def add_trainer(request):
    if request.method == 'POST':
        form = TrainerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')
    else:
        form = TrainerForm()
    
    return render(request, 'trainer_form.html', {'form': form})

@login_required
def edit_trainer(request, id):
    trainer = get_object_or_404(Trainer, pk=id)  # Obtener el entrenador por ID
    if request.method == 'POST':
        form = TrainerForm(request.POST, instance=trainer)  # Cargar el formulario con la instancia existente
        if form.is_valid():
            form.save()  # Guardar los cambios
            return redirect('pokedex:index')  # Redirigir a la página de inicio o donde prefieras
    else:
        form = TrainerForm(instance=trainer)  # Cargar el formulario con los datos actuales del entrenador

    return render(request, 'trainer_form.html', {'form': form})

@login_required
def delete_trainer(request, id):
    trainer = get_object_or_404(Trainer, pk=id)  # Obtener el entrenador por ID
    if request.method == 'POST':
        trainer.delete()  # Eliminar el entrenador
        return redirect('pokedex:index')  # Redirigir a la página de inicio o donde prefieras
    
    # Mostrar una página de confirmación antes de eliminar (opcional)
    return render(request, 'confirm_delete_trainer.html', {'trainer': trainer})
