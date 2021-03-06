# Generated by Django 4.0.6 on 2022-07-12 09:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_student_admission_date_student_updated_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('physics', models.BigIntegerField(blank=True, null=True)),
                ('chemistry', models.BigIntegerField(blank=True, null=True)),
                ('math', models.BigIntegerField(blank=True, null=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
            ],
        ),
    ]
