# Generated by Django 5.1.4 on 2024-12-10 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_mestredejogo_jogador_delete_aluno_delete_professor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mestredejogo',
            name='experiencia',
            field=models.TextField(),
        ),
    ]
