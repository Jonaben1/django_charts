from django.core.management.base import BaseCommand
from charts.models import Richest
import csv
import math


class Command(BaseCommand):
    help = 'Populate the database using a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('forbes_2022_billionaires.csv', type=str, help='The path to the CSV file')

    def handle(self, *args, **options):
        csv_file = options['forbes_2022_billionaires.csv']

        with open(csv_file, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                skip_row = False
                for value in row.values():
                    try:
                        if math.isnan(float(value)):
                            skip_row = True
                            break
                    except ValueError:
                        pass
                if skip_row:
                    continue
                net_worth = int(float(row['finalWorth']))
                obj, created = Richest.objects.get_or_create(
                    name=row['personName'],
                    gender=row['gender'],
                    net_worth=net_worth,
                    country=row['countryOfCitizenship'],
                    source=row['source']
                 )

        self.stdout.write(self.style.SUCCESS('Successfully populated the database'))
