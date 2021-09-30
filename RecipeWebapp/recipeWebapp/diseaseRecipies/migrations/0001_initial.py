# Generated by Django 3.2.7 on 2021-09-27 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45)),
                ('description', models.CharField(max_length=45, null=True)),
            ],
            options={
                'db_table': 'disease',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45)),
                ('email', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='Recipies',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=45)),
                ('image1', models.ImageField(null=True, upload_to='images/')),
                ('image2', models.ImageField(null=True, upload_to='images/')),
                ('image3', models.ImageField(null=True, upload_to='images/')),
                ('image4', models.ImageField(null=True, upload_to='images/')),
                ('disease', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='diseaseRecipies.disease')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='diseaseRecipies.user')),
            ],
            options={
                'db_table': 'recipies',
            },
        ),
    ]
