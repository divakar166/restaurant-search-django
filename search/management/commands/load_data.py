import csv
import json
from django.core.management.base import BaseCommand
from search.models import Restaurant

class Command(BaseCommand):
    help = 'Load data from CSV file'
    def handle(self, *args, **kwargs):
        file_path = 'data.csv'
        try:
            with open(file_path, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    full_details = row['full_details']
                    if not full_details.strip():
                        self.stdout.write(self.style.WARNING(f"Empty full_details in row {reader.line_num}, skipping row."))
                        continue
                    try:
                        full_details = json.loads(full_details)
                    except json.JSONDecodeError as e:
                        self.stdout.write(self.style.ERROR(f"JSONDecodeError in row {reader.line_num}: {e}"))
                        continue
                    Restaurant.objects.create(
                        id=row['id'],
                        name=row['name'],
                        location=row['location'],
                        items=row['items'],
                        lat_long=row['lat_long'],
                        full_details=full_details
                    )
            self.stdout.write(self.style.SUCCESS('Data loaded successfully'))
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f"File {file_path} not found"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"An error occurred: {e}"))
