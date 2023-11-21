from django.conf import settings
from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=50, verbose_name='название')
    description = models.TextField(verbose_name='описание', null=True, blank=True)
    status = models.BooleanField(default=False, verbose_name='статус')
    created_at = models.DateTimeField(auto_now=True, verbose_name='дата создания')
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь',
        null=True, blank=True)

    def __str__(self):
        return f"{self.title} ({self.description})"

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
