from django.db import migrations, models
import django.core.validators

class Migration(migrations.Migration):

    dependencies = [
        ('lifts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='liftattempt',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='videos/',
                validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4','mov','webm','m4v'])]),
        ),
    ]
