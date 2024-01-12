from django.db import models


class Pokemon(models.Model):
    title = models.CharField(max_length=200, verbose_name="Имя")
    title_en = models.CharField(max_length=200, null=True, blank=True, verbose_name="Имя (англ.)")
    title_jp = models.CharField(max_length=200, null=True, blank=True, verbose_name="Имя(яп.)")
    image = models.ImageField(upload_to='', null=True, blank=True, verbose_name="Изображение")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    prev_evolution = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True,
                                       related_name="next_evolutions", verbose_name="Из кого эволюционировал")

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, verbose_name="Покемон")
    lat = models.FloatField(verbose_name="Координаты широты")
    lon = models.FloatField(verbose_name="Координаты долготы")
    appeared_at = models.DateTimeField(verbose_name="Дата появления")
    disappeared_at = models.DateTimeField(verbose_name="Дата исчезновения")
    level = models.IntegerField(verbose_name="Уровень")
    health = models.IntegerField(verbose_name="Здоровье")
    strength = models.IntegerField(verbose_name="Сила")
    defence = models.IntegerField(verbose_name="Защита")
    stamina = models.IntegerField(verbose_name="Выносливость")
