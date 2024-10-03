from django.contrib import admin

from cats.models import Kitty, Breed, KittyRating


@admin.register(Kitty)
class KittyAdmin(admin.ModelAdmin):
    pass


@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    pass


@admin.register(KittyRating)
class KittyRatingAdmin(admin.ModelAdmin):
    pass
