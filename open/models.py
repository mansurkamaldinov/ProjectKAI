from django.db import models

class Articles(models.Model):
    title = models.CharField('Название Расписания',max_length=50)
    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписание'


class Employee(models.Model):
    name = models.CharField(max_length=100)
    colned = models.CharField("Количество уроков в неделю",max_length=50)
    сolden = models.CharField("Количество урооков в день",max_length=50)
    company = models.ForeignKey(Articles, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Классы'
        verbose_name_plural = 'Классы'



