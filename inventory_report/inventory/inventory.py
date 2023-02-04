import os
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


class ImporterFactory:
    @staticmethod
    def create_importer(path: str):
        _, extension = os.path.splitext(path)
        if extension == '.csv':
            return CsvImporter.import_data(path)
        elif extension == '.json':
            return JsonImporter.import_data(path)
        elif extension == '.xml':
            return XmlImporter.import_data(path)
        else:
            raise ValueError("Arquivo inválido")


class Inventory:
    @staticmethod
    def import_data(path: str, report_type: str):
        importer = ImporterFactory.create_importer(path)

        if report_type == 'simples':
            return SimpleReport.generate(importer)
        elif report_type == 'completo':
            return CompleteReport.generate(importer)
        else:
            raise ValueError(f'Unknown report type: {report_type}')
