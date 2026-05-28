from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_compra'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.IntegerField(
                    choices=[(1, '1 estrela'), (2, '2 estrelas'), (3, '3 estrelas'), (4, '4 estrelas'), (5, '5 estrelas')],
                    validators=[
                        django.core.validators.MinValueValidator(1),
                        django.core.validators.MaxValueValidator(5),
                    ]
                )),
                ('comentario', models.TextField(max_length=500)),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('compra', models.OneToOneField(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='avaliacao',
                    to='app.compra',
                )),
                ('produto', models.ForeignKey(
                    blank=True,
                    null=True,
                    on_delete=django.db.models.deletion.SET_NULL,
                    related_name='avaliacoes',
                    to='app.produto',
                )),
                ('usuario', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to=settings.AUTH_USER_MODEL,
                )),
            ],
        ),
    ]
