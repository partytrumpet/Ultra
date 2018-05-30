# Generated by Django 2.0.5 on 2018-05-30 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Colour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='DeliveryAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=200)),
                ('lastName', models.CharField(max_length=200)),
                ('address1', models.CharField(max_length=200)),
                ('address2', models.CharField(max_length=200)),
                ('address3', models.CharField(max_length=200)),
                ('stateCounty', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('postcode', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(default=0)),
                ('deliveryAddressId', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.DeliveryAddress')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('orderId', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.Order')),
            ],
        ),
        migrations.CreateModel(
            name='ProductColour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('colourId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Colour')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=200)),
                ('lastName', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('address1', models.CharField(max_length=200)),
                ('address2', models.CharField(max_length=200)),
                ('address3', models.CharField(max_length=200)),
                ('stateCounty', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('postcode', models.CharField(max_length=200)),
                ('admin', models.BooleanField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='typeId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.Type'),
        ),
        migrations.AddField(
            model_name='productcolour',
            name='productId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Product'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='productId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.Product'),
        ),
        migrations.AddField(
            model_name='deliveryaddress',
            name='userId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.User'),
        ),
    ]
