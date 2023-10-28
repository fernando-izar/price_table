# Generated by Django 4.2.6 on 2023-10-28 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product_category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('color', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='product_category.productcategory')),
            ],
        ),
    ]