from django.db import models


class Owner(models.Model):
    name = models.CharField('NAME', max_length=40, null=True)
    sale_opportunity = models.BooleanField('Sale Opportunity', default=True)


class Car(models.Model):
    COLOR_CHOICES = (
        ('YELLOW', 'YELLOW'),
        ('BLUE', 'BLUE'),
        ('GRAY', 'GRAY'),
    )

    MODEL_CHOICES = (
        ('HATCH', 'HATCH'),
        ('SEDAN', 'SEDAN'),
        ('CONVERTIBLE', 'CONVERTIBLE'),
    )

    name = models.CharField('NAME', max_length=40, null=True)
    color = models.CharField('COLOR', max_length=15, choices=COLOR_CHOICES, null=False)
    model = models.CharField('MODEL', max_length=15, choices=MODEL_CHOICES, null=False)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, null=False)
