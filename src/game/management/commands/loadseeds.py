import json
import os
from collections import defaultdict

import yaml
from django.apps import apps
from django.core.exceptions import ValidationError
from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Load data from YAML or JSON fixtures in a directory using the built-in loaddata command and validate instances afterward.'

    def add_arguments(self, parser):
        parser.add_argument('fixtures_dir', type=str, help='Path to the directory containing fixture files.')

    def handle(self, *args, **options):
        exception = None
        fixtures_dir = options['fixtures_dir']
        fixture_files = [
            os.path.join(fixtures_dir, f) for f in os.listdir(fixtures_dir) if
            os.path.isfile(os.path.join(fixtures_dir, f))
        ]

        # Use Django's built-in loaddata command to load all fixtures
        call_command('loaddata', fixture_files)

        all_data = []
        for fixture_file in fixture_files:
            all_data.extend(self.load_fixture_data(fixture_file))

        # Group entries by model
        grouped_entries = defaultdict(list)
        for entry in all_data:
            grouped_entries[entry['model']].append(entry)

        for model_path, entries in grouped_entries.items():
            # Get the model class
            app_name, model_name = model_path.split('.')
            model = apps.get_model(app_name, model_name)

            instances = model.objects.filter(pk__in=[entry['pk'] for entry in entries])
            for instance in instances:

                try:
                    instance.full_clean()
                except ValidationError as e:
                    print(f"Validation error for {model_name} instance: {e}")
                    instance.delete()
                    exception = exception or e

        if exception:
            raise exception

    def load_fixture_data(self, file_path):
        _, file_extension = os.path.splitext(file_path)
        with open(file_path, 'r') as file:
            if file_extension == '.json':
                return json.load(file)
            elif file_extension == '.yaml' or file_extension == '.yml':
                return yaml.safe_load(file)
            else:
                print(f"Unsupported file format: {file_path}")
                return []
