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
    cover = models.URLField()
    gallery = models.JSONField()
    trophy_count = models.IntegerField()
    price = models.IntegerField()
    trailer = models.JSONField()
    age_required = models.IntegerField()
    owner = models.ManyToManyField(User, through='GameOwnership')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class GameOwnership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'game')

class Trophy(models.Model):
    name = models.CharField(max_length=150)
    icon = models.URLField()
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    owner = models.ManyToManyField(User, through='UserTrophy')

    class Meta:
        ordering = ['game', 'name']

    def __str__(self):
        return self.name

class UserTrophy(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trophy = models.ForeignKey(Trophy, on_delete=models.CASCADE)
    achieved = models.BooleanField()

    class Meta:
        unique_together = ('user', 'trophy')

class GameCategory(models.Model):
    name = models.CharField(max_length=100)
    game = models.ManyToManyField(Game)

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
    game = models.ManyToManyField(Game)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=150)
    game = models.ManyToManyField(Game)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name