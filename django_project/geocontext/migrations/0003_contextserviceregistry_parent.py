# Generated by Django 2.0.6 on 2018-06-25 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('geocontext', '0002_auto_20180509_0923'),
    ]

    operations = [
        migrations.AddField(
            model_name='contextserviceregistry',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='geocontext.ContextServiceRegistry', verbose_name='The parent of this service registry'),
        ),
    ]
