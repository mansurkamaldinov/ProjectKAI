

from django.db import models

class Articles(models.Model):
    title = models.CharField('Название расписания',max_length=50)
    col = models.CharField('Колличество классов',max_length=250)
    col_subject = models.CharField('Колличество предметов',max_length=50)
    subjects=models.TextField('Перечислите предметы')

    def __str__(self):
        return f'Открытие{self.title}'
    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписание'
