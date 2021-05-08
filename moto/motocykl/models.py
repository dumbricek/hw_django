from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse


class Typ(models.Model):
    oznaceni_typu = models.CharField(max_length=50, unique=True, verbose_name="Označení typu zboží",
                            help_text='Zadejte text o maximální délce 50 znaků; text musí být jedinečný')
    OBLAST = (
        ('supersport', 'Supersport'),
        ('naháč', 'Naháč'),
        ('cross', 'Cross'),
        ('skútr', 'Skútr'),
        ('cestovní', 'Cestovní'),
        ('ostatní', 'Ostatní'),
    )
    oblast = models.CharField(max_length=20, choices=OBLAST, blank=True, default='Supersport', verbose_name="Oblast", help_text='Vyberte označení oblasti')

    class Meta:
        ordering = ["oznaceni_typu"]
        verbose_name = 'Typ'
        verbose_name_plural = 'Typy'

    def __str__(self):
        return f"{self.oznaceni_typu}, {self.oblast}"


class Motorky(models.Model):
    nazev = models.CharField(max_length=100, verbose_name="Název motorky", help_text='Zadejte text o maximální délce 100 znaků')
    popis = models.TextField(blank=True, null=True, verbose_name="Popis motorky")
    cena = models.FloatField(validators=[MinValueValidator(0.0)], null=True, help_text="Zadejte nezáporné desetinné číslo", verbose_name="Cena")
    STAV = (
        ('jako nová', 5),
        ('málo používaná', 4),
        ('často používaná', 3),
        ('opotřebovaná', 2),
        ('funkční vady', 1),
    )
    stav = models.IntegerField(choices=STAV, blank=True, default=3, verbose_name="Stav zboží", help_text='Vyberte označení stavu')
    foto = models.ImageField(upload_to='motorky/%Y/%m/%d/', blank=True, null=True, verbose_name="Fotka motorky")
    typ = models.ForeignKey(Typ, on_delete=models.RESTRICT)

    class Meta:
        ordering = ["-cena", "nazev"]
        verbose_name = 'Motorka'
        verbose_name_plural = 'Motorky'

    def __str__(self):
        return f"{self.nazev}, {self.cena}"

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])
