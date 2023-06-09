# Generated by Django 4.1.2 on 2022-10-24 04:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_project_tag_alter_review_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.ImageField(default='kurik.jpg', upload_to=''),
        ),
        migrations.AlterField(
            model_name='project',
            name='tag',
            field=models.ManyToManyField(blank=True, related_name='project_tag', to='projects.tag'),
        ),
        migrations.AlterField(
            model_name='review',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project_review', to='projects.project'),
        ),
        migrations.AlterField(
            model_name='review',
            name='value',
            field=models.CharField(choices=[('+', 'Ijobiy'), ('-', 'Salbiy')], max_length=50),
        ),
    ]
