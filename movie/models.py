from django.db import models
from django.utils import timezone
from accounts.models import CustomUser
from django.core.exceptions import ValidationError
from django.db.models import F, Avg



class Acteur(models.Model):
    nom = models.CharField(max_length=30, null=True, blank=True)
    prenom = models.CharField(max_length=50, null=True, blank=True)
    photo = models.ImageField(upload_to="acteur/", null=True, blank=True)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.nom + " " + self.prenom 



class Film(models.Model):
    titre = models.CharField(max_length=100)
    synopsis = models.TextField(null=True, blank=True)
    choix_genre = (
        ('Anime', 'Anime'),
        ('Action', 'Action'),
        ('Drame', 'Drame'),
        ('Comédie', 'Comédie'),
        ('Horreur', 'Horreur'),
    )
    genre = models.CharField(max_length=20, choices=choix_genre)
    date_sortie = models.DateField()
    duree = models.PositiveIntegerField()  
    casting = models.ForeignKey(Acteur, on_delete=models.SET_NULL, blank=True, null=True, related_name="cating") 
    image = models.ImageField(upload_to="film/", null=True, blank=True)
    ntmoy = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titre

    # Calcul automatique de la note moyenne
    def calculate_ntmoy(self):
        critiques = self.film.all()  # Utilisation du related_name 'film' pour accéder aux critiques
        moyenne = critiques.aggregate(Avg('note'))['note__avg']
        self.ntmoy = moyenne or 0
        self.save()

    # Méthode save pour s'assurer que la note moyenne est mise à jour à chaque modification du film
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.calculate_ntmoy()


class Critique(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name="film", null=True, blank=True)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="owner", null=True, blank=True)
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=2000)
    note = models.IntegerField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True, null=True)  
    updated_at = models.DateTimeField(auto_now=True, null=True) 

    def __str__(self):
        return f"{self.owner}  {self.title}/{self.note}"

    def clean(self):
        super().clean()
        if self.note < 0 or self.note >= 6:
            raise ValidationError("la note ne doit pas être supérieure à 5")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.film.calculate_ntmoy()  



class Comment(models.Model):
    critique = models.ForeignKey(Critique, on_delete=models.CASCADE, null=True)
    utilisateur = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    text = models.TextField(max_length=1000)
    publication = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.utilisateur} : {self.text}"
