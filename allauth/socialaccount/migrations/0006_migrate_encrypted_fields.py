# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


def update(apps, schema_editor):
    # Can't figure out how to get allauth models with apps.get_model
    SocialAccount = [m for m in apps.get_models() if m.__name__=='SocialAccount'][0]
    SocialApp = [m for m in apps.get_models() if m.__name__=='SocialApp'][0]
    SocialToken = [m for m in apps.get_models() if m.__name__=='SocialToken'][0]

    for acc in SocialAccount.objects.all():
        acc.extra_data_encrypted = acc.extra_data
        acc.save()

    for app in SocialApp.objects.all():
        app.client_id_encrypted = app.client_id
        app.key_encrypted = app.key
        app.secret_encrypted = app.secret
        app.save()

    for tok in SocialToken.objects.all():
        tok.token_encrypted = tok.token
        tok.token_secret_encrypted = tok.token_secret
        tok.save()


class Migration(migrations.Migration):

    dependencies = [
        ('socialaccount', '0005_auto_20200209_1049'),
    ]

    operations = [
        migrations.RunPython(update)
    ]
