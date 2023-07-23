# Generated by Django 4.2.2 on 2023-07-23 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_alter_like_artist_alter_like_track'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='core.artist'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='track',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='core.track'),
        ),
        migrations.AlterField(
            model_name='repost',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reposts', to='core.artist'),
        ),
        migrations.AlterField(
            model_name='repost',
            name='track',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reposts', to='core.track'),
        ),
        migrations.AlterField(
            model_name='socialnetwork',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='socialnetworks', to='core.artist'),
        ),
    ]
