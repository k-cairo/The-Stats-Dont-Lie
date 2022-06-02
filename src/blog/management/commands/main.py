from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Update cards and corners Datas'

    def handle(self, *args, **options):
        # TODO
        self.stdout.write('Cards and Corners Datas Updated Successfully')