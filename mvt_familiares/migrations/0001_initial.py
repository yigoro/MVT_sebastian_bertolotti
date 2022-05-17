from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Familiar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('parentezco', models.CharField(max_length=25)),
                ('fecha_nacimiento', models.DateField()),
                ('dni', models.CharField(max_length=8)),
            ],
        ),
    ]
