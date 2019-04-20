# Generated by Django 2.1.7 on 2019-04-02 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0010_auto_20190401_2251'),
    ]

    operations = [
        migrations.CreateModel(
            name='allData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isActive', models.BooleanField(default=True, verbose_name='状态')),
            ],
            options={
                'verbose_name': '总表',
                'verbose_name_plural': '总表',
            },
        ),
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(max_length=100, verbose_name='数量')),
                ('isActive', models.BooleanField(choices=[(0, '未安排'), (1, '已安排'), (2, '待寄出'), (3, '待付款'), (4, '已完结')], default=0, verbose_name='状态')),
                ('startTime', models.DateTimeField(auto_now_add=True, verbose_name='接单时间')),
                ('endTime', models.DateTimeField(verbose_name='预期完结时间')),
            ],
            options={
                'verbose_name': '总表',
                'verbose_name_plural': '总表',
            },
        ),
        migrations.RemoveField(
            model_name='customer',
            name='unit',
        ),
        migrations.RemoveField(
            model_name='user',
            name='customer',
        ),
        migrations.AddField(
            model_name='unit',
            name='isActive',
            field=models.BooleanField(default=True, verbose_name='状态'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='uphone',
            field=models.IntegerField(max_length=50, verbose_name='手机号'),
        ),
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(on_delete=True, to='index.customer'),
        ),
        migrations.AddField(
            model_name='order',
            name='unit',
            field=models.ForeignKey(on_delete=True, to='index.unit'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=True, to='index.user'),
        ),
        migrations.AddField(
            model_name='alldata',
            name='customer',
            field=models.ForeignKey(on_delete=True, to='index.customer'),
        ),
        migrations.AddField(
            model_name='alldata',
            name='unit',
            field=models.ForeignKey(on_delete=True, to='index.unit'),
        ),
        migrations.AddField(
            model_name='alldata',
            name='user',
            field=models.ForeignKey(on_delete=True, to='index.user'),
        ),
    ]