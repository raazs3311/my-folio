# Generated by Django 4.0.2 on 2022-03-08 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raj', '0005_alter_images_img_alter_projectimg_proimg'),
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_img', models.FileField(upload_to='static/image')),
            ],
        ),
    ]