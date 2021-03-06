# Generated by Django 3.1.2 on 2020-10-14 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meter_number', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('quiz', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ContentManager.term')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('option1', models.CharField(blank=True, max_length=250, null=True)),
                ('option2', models.CharField(blank=True, max_length=250, null=True)),
                ('option3', models.CharField(blank=True, max_length=250, null=True)),
                ('option4', models.CharField(blank=True, max_length=250, null=True)),
                ('correct_answer', models.CharField(blank=True, max_length=250, null=True)),
                ('quiz', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ContentManager.quiz')),
            ],
        ),
    ]
