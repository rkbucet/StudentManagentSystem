# Generated by Django 4.2.2 on 2023-06-26 05:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('City_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Course_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Student_name', models.CharField(max_length=50)),
                ('Student_phone', models.BigIntegerField()),
                ('Student_email', models.CharField(max_length=100)),
                ('Student_fees', models.IntegerField()),
                ('Student_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentapp.city')),
                ('Student_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentapp.course')),
            ],
        ),
    ]