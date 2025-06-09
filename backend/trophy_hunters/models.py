from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    steam_processed = models.BooleanField(default=False)
    steam_id = models.BigIntegerField(null=True,blank=True)
    avatar = models.ImageField(upload_to='profile_pictures', null=True, blank=True)
    banner = models.ImageField(upload_to='profile_banners', null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['user']

    def __str__(self):
        return self.user.username

class Game(models.Model):
    app_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    cover = models.URLField(null=True, blank=True)
    trophy_count = models.IntegerField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    is_free = models.BooleanField(null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    categories = models.ManyToManyField('Category', related_name='games_with_category', blank=True)
    developers = models.ManyToManyField('Developer', related_name='games_developed', blank=True)
    publishers = models.ManyToManyField('Publisher', related_name='games_published', blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Gallery(models.Model):
    url = models.URLField()
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='images')

    class Meta:
        ordering = ['game']

    def __str__(self):
        return self.game.name

class Trailer(models.Model):
    url = models.URLField()
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='movies')

    class Meta:
        ordering = ['game']

    def __str__(self):
        return self.game.name

class GameOwnership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_games')
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='owners')

    class Meta:
        unique_together = ('user', 'game')

    def __str__(self):
        return f'{self.user.username} owns {self.game.name}'

class Trophy(models.Model):
    name = models.TextField()
    api_name = models.TextField(null=True, blank=True)
    blocked_icon = models.URLField(null=True, blank=True)
    unlocked_icon = models.URLField(null=True, blank=True)
    hidden = models.BooleanField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='trophies')

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
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class DLC(models.Model):
    app_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='dlcs')

    class Meta:
        ordering = ['game']

    def __str__(self):
        return self.name

class Developer(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class New(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='news')

    def __str__(self):
        return self.title