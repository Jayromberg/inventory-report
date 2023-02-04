import os
import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @staticmethod
    def import_data(path: str):
        _, extension = os.path.splitext(path)

        if extension != '.json':
            raise ValueError("Arquivo inválido")

        with open(path) as file:
            dicts = json.load(file)

        return dicts
