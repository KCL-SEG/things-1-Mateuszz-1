from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Thing(models.Model):
    name = models.CharField(
        max_length = 30,
        unique = True,
        blank = False
        )
    description = models.CharField(
        max_length = 120,
        blank = True
    )
    quantity = models.IntegerField(
        validators = [
            MaxValueValidator(
                limit_value = 100
            ),
            MinValueValidator(
                limit_value = 0
            )
        ]
    )
