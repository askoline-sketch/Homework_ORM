import csv

from django.core.management.base import BaseCommand

from phones.models import Phone


class Command(BaseCommand):
    help = 'Импорт данных из csv файла в базу данных'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        # Кодировку лучше указать явно, чтобы избежать проблем с кириллицей
        with open('phones.csv', 'r', encoding='utf-8') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            # Используем update_or_create, чтобы избежать ошибок
            # при повторном запуске скрипта (дубликатов ID)
            Phone.objects.update_or_create(
                id=phone['id'],
                defaults={
                    'name': phone['name'],
                    'price': int(phone['price']),
                    'image': phone['image'],
                    'release_date': phone['release_date'],
                    'lte_exists': phone['lte_exists'] == 'True',
                }
            )

        self.stdout.write(
            self.style.SUCCESS('Данные успешно загружены в базу!')
        )