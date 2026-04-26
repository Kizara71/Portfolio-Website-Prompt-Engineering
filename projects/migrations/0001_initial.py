from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('thumbnail', models.ImageField(upload_to='portfolio/thumbnails/')),
                ('description', models.TextField()),
                ('problem_solved', models.TextField()),
                ('my_role', models.TextField()),
                ('key_features', models.TextField(help_text='Enter as a bulleted list or comma separated.')),
                ('tools_used', models.CharField(max_length=300)),
                ('github_link', models.URLField(blank=True, null=True)),
                ('playable_link', models.URLField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
