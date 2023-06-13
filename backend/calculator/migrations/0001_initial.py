from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CalculatorTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=255)),
                ('status', models.IntegerField(choices=[(0, 'New'), (1, 'Running'), (2, 'Finished'), (3, 'Failed')], db_index=True, default=0)),
            ],
        ),
        migrations.CreateModel(
            name='CalculatorResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('column', models.IntegerField()),
                ('result', models.IntegerField()),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='results', to='calculator.calculatortask')),
            ],
        ),
    ]
