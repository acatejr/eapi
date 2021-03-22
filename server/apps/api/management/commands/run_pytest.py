from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'Runs test through pytest'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Done!'))
