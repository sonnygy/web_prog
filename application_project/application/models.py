from django.db import models

class Application(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    phone = models.CharField(max_length=15, verbose_name="Телефон")
    email = models.EmailField(blank=True, null=True, verbose_name="Почта")
    comment = models.TextField(blank=True, null=True, verbose_name="Комментарий")

    service_choices = [
        ('diagnostics', 'Диагностика'),
        ('repair', 'Ремонт'),
        ('maintenance', 'ТО'),
        ('tire', 'Шиномонтаж'),
        ('other', 'Другое'),
    ]
    service = models.CharField(max_length=50, choices=service_choices, default='diagnostics', verbose_name="Услуга")
    time = models.DateTimeField(verbose_name="Время")

    notification_choices = [
        ('call', 'Звонок'),
        ('sms', 'SMS'),
        ('email', 'Email'),
    ]
    notification = models.CharField(max_length=20, choices=notification_choices, default='sms', verbose_name="Уведомление")

    def __str__(self):
        return f"{self.name} - {self.service} - {self.time}"
