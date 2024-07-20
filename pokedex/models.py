from django.db import models

class Trainer(models.Model):
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    birth_date = models.DateField(null=False)
    level = models.IntegerField(default=1)
    
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

class Pokemon (models.Model):
    name = models.CharField(max_length=30, null=False)
    POKEMON_TYPES = {
        ('A', 'Agua'),
        ('F', 'Fuego'),
        ('T', 'Tierra'),
        ('P', 'Planta'),
        ('E', 'Eléctrico'),
        ('L', 'Lagartija'),
        ('H', 'Hielo'),
        ('S', 'Siniestro'),   
    }
    
    type = models.CharField(max_length=30, choices=POKEMON_TYPES, null=False)
    weight = models.DecimalField(null=False, default=1, max_digits=4, decimal_places=2)
    height = models.DecimalField(null=False, default=1, max_digits=4, decimal_places=2)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)#con el cascade se borra el entrenador y todos los pokemones es necesario usar 
    #una llave foranea directamente a Trainer
    picture = models.ImageField(upload_to='pokemon_images')
    #una llave foranea directamente a Trainer
    
    
    def __str__(self) -> str:
        return self.name 