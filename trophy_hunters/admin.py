from django.contrib import admin
from .models import  *

admin.site.register(
    [
        Profile,
        Game,
        Trophy,
        GameOwnership,
        UserTrophy,
        DLC,
        Developer,
        Publisher,
    ]
)