# Generated by Django 2.1.7 on 2019-03-31 02:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=11, verbose_name='账号')),
                ('upwd', models.CharField(max_length=20, verbose_name='密码')),
                ('isActive', models.BooleanField(default=True, verbose_name='状态')),
            ],
            options={
                'verbose_name': '客户信息',
                'verbose_name_plural': '客户信息',
            },
        ),
        migrations.RemoveField(
            model_name='customer',
            name='upwd',
        ),
        migrations.AddField(
            model_name='customer',
            name='unit',
            field=models.ManyToManyField(to='index.unit'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='uphone',
            field=models.IntegerField(max_length=11, verbose_name='手机号'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='uqq',
            field=models.IntegerField(max_length=15, verbose_name='QQ'),
        ),
        migrations.AddField(
            model_name='user',
            name='custom',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='index.customer'),
        ),
    ]
