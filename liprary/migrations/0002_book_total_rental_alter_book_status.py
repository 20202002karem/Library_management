# Generated by Django 4.1.6 on 2023-02-21 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('liprary', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='total_rental',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='status',
            field=models.CharField(choices=[('sold', 'sold'), ('rental', 'rental'), ('avilble', 'avilble')], max_length=50),
        ),
    ]
