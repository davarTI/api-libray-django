# Generated by Django 2.2.6 on 2019-11-13 23:58

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='editorial',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='editoriales.Editorial'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='fecha_pub',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 13, 23, 58, 4, 692373, tzinfo=utc), verbose_name='date published'),
        ),
    ]