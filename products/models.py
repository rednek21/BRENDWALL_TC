from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=64, verbose_name='Название продукта', unique=True)
    price = models.FloatField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        db_table = 'products'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

        # Можно индексировать название на случай, если необходим поиск конкретного продукта
        # indexes = [
        #     models.Index(fields=["title", "title"]),
        # ]
