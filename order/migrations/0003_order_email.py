# Generated by Django 4.0.4 on 2022-05-18 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_alter_orderitem_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='email',
            field=models.EmailField(default='ade@m.com', max_length=254),
            preserve_default=False,
        ),
    ]
