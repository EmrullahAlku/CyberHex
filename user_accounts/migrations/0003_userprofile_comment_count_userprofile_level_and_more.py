# Generated by Django 5.1.2 on 2024-11-16 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_accounts', '0002_userprofile_delete_role_remove_user_bio_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='comment_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='level',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='like_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='post_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]