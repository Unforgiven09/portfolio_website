from django.db import models


class Parts(models.Model):
    product = models.OneToOneField('main.Products', on_delete=models.CASCADE, related_name='parts', verbose_name='Товар')
    socket_mb2cpu = models.TextField(blank=True, verbose_name='Разъем материнка - процессор')
    socket_mb2gpu = models.TextField(blank=True, verbose_name='Разъем материнка - видеокарта')
    socket_mb2ssd = models.TextField(blank=True, verbose_name='Разъем материнка - ссд')
    socket_mb2ram = models.TextField(blank=True, verbose_name='Разъем материнка - оперативка')
    socket_mb2psu = models.TextField(blank=True, verbose_name='Разъем материнка - блок питания')
    chipset = models.TextField(blank=True, verbose_name='Чипсет') # для материнки
    usb_ports = models.IntegerField(null=True, verbose_name='ЮСБ разъемы')  # для материнки
    frequency = models.IntegerField(null=True, verbose_name='Частота')  # для процессора или видеокарты
    recommended_power_supply = models.IntegerField(null=True, verbose_name='Рекомендованая мощность питания')  # для процессора и видеокарты
    psu_power = models.IntegerField(null=True, verbose_name='Мощность блока питания')  # для блока питания
    memory_size = models.IntegerField(null=True, verbose_name='Объем памяти')  # для ссд или оперативки
    model_series = models.TextField(blank=True, verbose_name='Серия модели')

    class Meta:
        verbose_name = 'Комплектующие'
        verbose_name_plural = 'Комплектующие'
        ordering = ['product']
