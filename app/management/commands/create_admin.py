from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Cria ou redefine o usuário administrador padrão do sistema'

    def handle(self, *args, **kwargs):
        username = 'Admin'
        password = 'Admin@123'
        email = 'admin@steamkeyhub.com'

        user, created = User.objects.get_or_create(username=username)
        user.email = email
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save()

        if created:
            self.stdout.write(self.style.SUCCESS(
                f'Usuário "{username}" criado com sucesso!\n'
                f'  Login: {username}\n'
                f'  Senha: {password}\n'
                f'  Acesso: /dashboard/'
            ))
        else:
            self.stdout.write(self.style.WARNING(
                f'Usuário "{username}" já existia — senha e permissões atualizadas.\n'
                f'  Login: {username}\n'
                f'  Senha: {password}'
            ))

        # Avisa sobre outros superusuários existentes
        outros = User.objects.filter(is_superuser=True).exclude(username=username)
        if outros.exists():
            nomes = ', '.join(outros.values_list('username', flat=True))
            self.stdout.write(self.style.WARNING(
                f'\nAtenção: outros superusuários encontrados: {nomes}\n'
                f'Se quiser remover os duplicados, faça pelo Django Admin (/admin/) ou via shell.'
            ))
