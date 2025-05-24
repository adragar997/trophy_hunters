from django.contrib import admin
from .models import  *

admin.site.register(
    [
        Profile,
        Game,
        Trophy,
        Category,
        GameOwnership,
        UserTrophy,
        DLC,
        Developer,
        Publisher,
        Trailer,
        Gallery,
        New,
    ]
)