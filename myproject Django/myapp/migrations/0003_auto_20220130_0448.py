# Generated by Django 3.2.8 on 2022-01-30 07:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20220130_0423'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=128)),
                ('monotributista', models.BooleanField()),
            ],
        ),
        migrations.AlterField(
            model_name='curso',
            name='inscriptos',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='curso',
            name='nombre',
            field=models.CharField(max_length=128),
        ),
        migrations.AddField(
            model_name='curso',
            name='profesor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.profesor'),
        ),
    ]
