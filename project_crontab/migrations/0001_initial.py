# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-08-01 14:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('asset', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CrontabCmd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cmd', models.TextField(verbose_name='\u624b\u52a8\u586b\u5165\u7684\u547d\u4ee4')),
                ('auto_cmd', models.TextField(verbose_name='\u81ea\u52a8\u8865\u5168\u7684\u547d\u4ee4')),
                ('frequency', models.CharField(max_length=16, verbose_name='\u6267\u884c\u9891\u7387')),
                ('cmd_status', models.IntegerField(choices=[(1, '\u6682\u505c\u4e2d'), (2, '\u8fd0\u884c\u4e2d')], default=1, verbose_name='\u72b6\u6001')),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='\u521b\u5efa\u65e5\u671f')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='\u6700\u540e\u66f4\u65b0\u65e5\u671f')),
                ('last_run_result', models.CharField(blank=True, max_length=16, null=True, verbose_name='\u4e0a\u6b21\u6267\u884c\u7ed3\u679c')),
                ('last_run_time', models.DateTimeField(blank=True, null=True, verbose_name='\u4e0a\u6b21\u6267\u884c\u65f6\u95f4')),
                ('creator', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='creator_of_crontab', to=settings.AUTH_USER_MODEL, verbose_name='\u521b\u5efa\u8005')),
                ('svn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='svn_of_crontab', to='asset.crontab_svn', verbose_name='Crontab\u6240\u5c5eSVN')),
                ('updater', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='updater_of_crontab', to=settings.AUTH_USER_MODEL, verbose_name='\u6700\u540e\u66f4\u65b0\u8005')),
            ],
            options={
                'verbose_name': 'crontab\u547d\u4ee4',
                'verbose_name_plural': 'crontab\u547d\u4ee4',
            },
        ),
    ]