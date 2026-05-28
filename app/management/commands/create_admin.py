from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Cria o usuário administrador padrão do sistema'

    def handle(self, *args, **kwargs):
        username = 'Admin'
        password = 'Admin@123'
        email = 'admin@steamkeyhub.com'

        if User.objects.filter(username=username).exists():
            self.stdout.write(self.style.WARNING(
                f'Usuário "{username}" já existe. Nenhuma ação realizada.'
            ))
            return

        User.objects.create_superuser(
            username=username,
            email=email,
            password=password,
        )
        self.stdout.write(self.style.SUCCESS(
            f'Usuário "{username}" criado com sucesso!\n'
            f'  Login:  {username}\n'
            f'  Senha:  {password}\n'
            f'  Acesso: /dashboard/'
        ))
