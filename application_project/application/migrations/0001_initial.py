# Generated by Django 5.2.2 on 2025-06-06 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('phone', models.CharField(max_length=15, verbose_name='Телефон')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Почта')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
                ('service', models.CharField(choices=[('diagnostics', 'Диагностика'), ('repair', 'Ремонт'), ('maintenance', 'ТО'), ('tire', 'Шиномонтаж'), ('other', 'Другое')], default='diagnostics', max_length=50, verbose_name='Услуга')),
                ('time', models.DateTimeField(verbose_name='Время')),
                ('notification', models.CharField(choices=[('call', 'Звонок'), ('sms', 'SMS'), ('email', 'Email')], default='sms', max_length=20, verbose_name='Уведомление')),
            ],
        ),
    ]
