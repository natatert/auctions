from django.db import models


class Auction(models.Model):
    AUCTION_STATUSES = (
        ('past', 'Прошедший'),
        ('active', 'Активный'),
        ('upcoming', 'Предстоящий'),
    )
    name = models.CharField('Название', max_length=50)
    status = models.CharField('Статус', max_length=8, choices=AUCTION_STATUSES)
    address = models.CharField('Адрес', max_length=40)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Аукцион'
        verbose_name_plural = 'Аукционы'


class Bidder(models.Model):
    name = models.CharField('Участник', max_length=40)
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Участник'
        verbose_name_plural = 'Участники'
