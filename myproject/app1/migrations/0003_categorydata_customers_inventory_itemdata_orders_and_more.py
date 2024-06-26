# Generated by Django 5.0.4 on 2024-04-25 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_sellerdata_remove_admindata_id_alter_admindata_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='categorydata',
            fields=[
                ('category', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('total_products', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='customers',
            fields=[
                ('Customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('contact', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('pincode', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='inventory',
            fields=[
                ('product_id', models.IntegerField(primary_key=True, serialize=False)),
                ('stock_quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='itemdata',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('Description', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('warranty', models.CharField(max_length=100)),
                ('Category', models.CharField(max_length=100)),
                ('inventory_quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_id', models.IntegerField()),
                ('order_date', models.DateField()),
                ('total_amt', models.IntegerField()),
                ('status', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='sellerdata',
            name='seller_credential',
        ),
        migrations.AddField(
            model_name='sellerdata',
            name='gst_number',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='sellerdata',
            name='pincode',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='sellerdata',
            name='email',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='sellerdata',
            name='name',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
