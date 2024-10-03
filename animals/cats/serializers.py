from rest_framework import serializers

from cats.models import Kitty, Breed, KittyRating


class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = '__all__'


class KittySerializer(serializers.ModelSerializer):
    """
    Сериализатор модели Kitty с доп. опциями:
    - Имя владельца
    - Название породы
    - Авто-владелец
    - Средний рейтинг котёнка
    """
    breed_name = serializers.SerializerMethodField()
    owner_name = serializers.SerializerMethodField()
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    avg_rating = serializers.SerializerMethodField()

    class Meta:
        model = Kitty
        fields = '__all__'

    @staticmethod
    def get_breed_name(obj):
        return obj.breed.name

    @staticmethod
    def get_owner_name(obj):
        return obj.owner.username

    @staticmethod
    def get_avg_rating(obj):
        kitty_rating = 'Нет рейтинга.'
        rating_list = obj.ratings.all()
        if rating_list:
            kitty_rating = (
                    sum(
                        [i.rating for i in rating_list]
                    ) // rating_list.count()
            )
        return kitty_rating


class KittyRatingSerializer(serializers.ModelSerializer):
    """
    Сериализатор модели KittyRating с доп. опциями:
    - Имя оценщика
    - Оценщик
    """
    owner_name = serializers.SerializerMethodField()
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = KittyRating
        fields = '__all__'

    @staticmethod
    def get_owner_name(obj):
        return obj.owner.username
