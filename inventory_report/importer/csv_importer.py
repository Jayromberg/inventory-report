import os
import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @staticmethod
    def import_data(path: str):
        _, extension = os.path.splitext(path)

        if extension != '.csv':
            raise ValueError("Arquivo inválido")

        with open(path) as file:
            reader = csv.DictReader(file)
            dicts = [dict(row) for row in reader]

        return dicts
