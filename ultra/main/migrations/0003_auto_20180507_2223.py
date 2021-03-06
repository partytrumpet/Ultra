# Generated by Django 2.0.5 on 2018-05-07 21:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_product_colour'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='order',
            name='deliveryAddressId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.DeliveryAddress'),
        ),
        migrations.AlterField(
            model_name='order',
            name='userId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.User'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='orderId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.Order'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='productId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.Product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.FileField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='typeId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.Type'),
        ),
        migrations.AddField(
            model_name='productimage',
            name='productId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.Product'),
        ),
    ]
