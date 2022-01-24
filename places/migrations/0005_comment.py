# Generated by Django 3.1 on 2022-01-20 07:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_auto_20220116_1951'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('body', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('cur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='places.placing')),
            ],
        ),
    ]
