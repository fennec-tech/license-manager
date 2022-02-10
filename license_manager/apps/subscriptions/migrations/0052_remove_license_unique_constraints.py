# Generated by Django 3.2.11 on 2022-02-15 14:09

from django.db import migrations, models
import license_manager.apps.subscriptions.utils


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0051_remove_subscriptionplan_deprecated_columns'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalnotification',
            name='last_sent',
            field=models.DateTimeField(default=license_manager.apps.subscriptions.utils.localized_utcnow, help_text='Date of the last time a notifcation was sent.'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='last_sent',
            field=models.DateTimeField(default=license_manager.apps.subscriptions.utils.localized_utcnow, help_text='Date of the last time a notifcation was sent.'),
        ),
        migrations.AlterUniqueTogether(
            name='license',
            unique_together=set(),
        ),
    ]
