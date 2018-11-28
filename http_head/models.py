from django.db import models
from django.contrib.postgres.fields import JSONField


class HttpHead(models.Model):
    data = JSONField()
    timestamp = models.DateField(auto_now_add=True)
    
    
    class Meta:
        verbose_name = 'Запрос к сайту'
        verbose_name_plural = 'Запросы к сайту'
        ordering = ['-timestamp']

    def __str__(self):
        return 'Запрос от {} '.format(self.timestamp)
    
