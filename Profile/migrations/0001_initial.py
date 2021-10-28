# Generated by Django 3.2.8 on 2021-10-28 15:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('SocialNetworks', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('FaceBook', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SocialNetworks.vkmodel')),
                ('instagram', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SocialNetworks.facebookmodel')),
                ('twitter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SocialNetworks.twittermodel')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('vk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SocialNetworks.instagrammodel')),
            ],
        ),
    ]
