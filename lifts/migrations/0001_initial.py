from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='LiftAttempt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lift_type', models.CharField(choices=[
                    ('przysiad', 'Przysiad'),
                    ('wyciskanie', 'Wyciskanie'),
                    ('martwy_ciag', 'Martwy ciąg')
                ], max_length=20)),
                ('weight_kg', models.DecimalField(decimal_places=2, max_digits=6)),
                ('date', models.DateField()),
                ('notes', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['-date', '-weight_kg'],
            },
        ),
    ]
