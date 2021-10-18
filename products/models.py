from django.db import models

class Wein(models.Model):
    WINZER_CHOICES = (
            ('ASC', 'Arndt Schnabel'),
            ('ASE', 'Andreas Schnabel'),
            ('GRO', 'Eckehart Groehl'),
            ('KRO', 'Markus Krollmann'),
            ('PSC', 'Philip Schnabel St. Martinshof'),
            ('SEY', 'Seyberth'),
            ('WHS', 'Winzer Hof Schnabel'),
    )
    WEINART_CHOICES = (
            ('rot', 'rot'),
            ('rose', 'rose'),
            ('weiss', 'weiss'),
            ('schaumwein-rot', 'schaumwein-rot'),
            ('schaumwein-rose', 'schaumwein-rose'),
            ('schaumwein-weiss', 'schaumwein-weiss'),
    )
    REBSORTE_CHOICES = (
            # weisse Rebsorten
            ('Riesling', 'Riesling'),
            ('Mueller-Thurgau', 'Mueller-Thurgau'),
            ('Silvaner', 'Silvaner'),
            ('Kerner', 'Kerner'),
            ('Weissburgunder', 'Weissburgunder'),
            ('Grauburgunder', 'Grauburgunder'),
            ('Bacchus', 'Bacchus'),
            ('Scheurebe', 'Scheurebe'),
            ('Huxelrebe', 'Huxelrebe'),
            ('Gewuerztraminer', 'Gewuerztraminer'),
            ('Chardonnay', 'Chardonnay'),
            ('Sauvignon Blanc', 'Sauvignon Blanc'),
            # rote Rebsorten
            ('Spaetburgunder', 'Spaetburgunder'),
            ('Dornfelder', 'Dornfelder'),
            ('Portugieser', 'Portugieser'),
            ('Schwarzriesling', 'Schwarzriesling'),
            ('Regent', 'Regent'),
            ('Saint Laurent', 'Saint Laurent'),
            ('Cabernet Sauvignon', 'Cabernet Sauvignon'),
            ('Merlot', 'Merlot'),
    )
    AUSBAU_CHOICES = (
            ('TR', 'trocken/herb'),
            ('HTR', 'halbtrocken/feinherb'),
            ('M', 'mild/suess'),
    )
    LAND_CHOICES = (
            ('DE', 'Deutschland'),
            ('AT', 'Oesterreich'),
    )
    REGION_CHOICES =(
            ('Rheinhessen', 'Rheinhessen'),
            ('Rheingau', 'Rheingau'),
            ('Mittelrhein', 'Mittelrhein'),
            ('Mosel', 'Mosel'),
            ('Nahe', 'Nahe'),
            ('Pfalz', 'Pfalz'),
            ('Weinfranken', 'Weinfranken'),
            ('Baden', 'Baden'),
    )
    artikelnr = models.IntegerField()
    titel = models.CharField(max_length=100)
    winzer = models.CharField(max_length=3, choices=WINZER_CHOICES)
    weinart = models.CharField(max_length=20, choices=WEINART_CHOICES)
    rebsorte = models.CharField(max_length=30, choices=REBSORTE_CHOICES)
    ausbau = models.CharField(max_length=20, choices=AUSBAU_CHOICES)
    land = models.CharField(max_length=20, choices=LAND_CHOICES)
    region = models.CharField(max_length=30, choices=REGION_CHOICES)
    jahrgang = models.IntegerField()
    inhalt = models.DecimalField(max_digits=3, decimal_places=2)
    alk = models.DecimalField(max_digits=3, decimal_places=1)
    saeure = models.DecimalField(max_digits=2, decimal_places=1)
    restzucker = models.DecimalField(max_digits=2, decimal_places=1)
    sulfite = models.BooleanField()
    added = models.DateTimeField(auto_now=True)
