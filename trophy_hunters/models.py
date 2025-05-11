from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    avatar = models.ImageField(upload_to='profile_pictures')
    banner = models.ImageField(upload_to='profile_banners')
    birth_date = models.DateField()
    bio = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['user']

    def __str__(self):
        return self.user.username

class Game(models.Model):
    app_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150)
    cover = models.URLField(null=True, blank=True)
    trophy_count = models.IntegerField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)
    age_required = models.IntegerField(null=True, blank=True)
    category = models.ManyToManyField('Category', related_name='games_with_category')
    developer = models.ManyToManyField('Developer', related_name='games_developed')
    publisher = models.ManyToManyField('Publisher', related_name='games_published')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Gallery(models.Model):
    url = models.URLField()
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    class Meta:
        ordering = ['game']

    def __str__(self):
        return self.game.name

class Trailer(models.Model):
    url = models.URLField()
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    class Meta:
        ordering = ['game']

    def __str__(self):
        return self.game.name

class GameOwnership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_games')
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    date_acquired = models.DateField()

    class Meta:
        unique_together = ('user', 'game')
        ordering = ['date_acquired']

    def __str__(self):
        return f'{self.user.username} owns {self.game.name}'

class Trophy(models.Model):
    name = models.CharField(max_length=150)
    icon = models.URLField()
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    class Meta:
        ordering = ['game', 'name']

    def __str__(self):
        return self.name

class UserTrophy(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_trophies')
    trophy = models.ForeignKey(Trophy, on_delete=models.CASCADE)
    achieved = models.BooleanField()

    class Meta:
        unique_together = ('user', 'trophy')

    def __str__(self):
        return f"{self.user.username} - {self.trophy.name} ({'✓' if self.achieved else '✗'})"

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class DLC(models.Model):
    app_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    class Meta:
        ordering = ['game']

    def __str__(self):
        return self.name

class Developer(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name