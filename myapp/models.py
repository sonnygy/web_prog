from django.db import models


class Application(models.Model):
  name = models.CharField(max_length=100)
  phone = models.CharField(max_length=15)
  email = models.EmailField(blank=True, null=True)
  car = models.CharField(max_length=100, null=True, blank=True)
  year = models.IntegerField(null=True, blank=True)
  service_choices = [
      ('diagnostics', 'Диагностика'),
      ('repair', 'Ремонт'),
      ('maintenance', 'Техническое обслуживание'),
      ('tire', 'Шиномонтаж'),
      ('other', 'Другое'),
  ]
  service = models.CharField(max_length=50, choices=service_choices, default='diagnostics')

  time = models.DateTimeField()

  notification_choices = [
      ('call', 'Звонок'),
      ('sms', 'SMS'),
      ('email', 'Email'),
  ]
  notification = models.CharField(max_length=20, choices=notification_choices, default = 'sms')

  def __str__(self):
    return f"{self.name} {self.phone} — {self.service} ({self.time})"
