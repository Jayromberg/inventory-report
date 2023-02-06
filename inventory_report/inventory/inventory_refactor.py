from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class InventoryRefactor:
    def __init__(self, importer):
        self.importer = importer
        self.data = []

    def import_data(self, path: str, report_type: str):
        print(self.importer)
        inventory = self.importer.import_data(path)
        self.data += inventory

        if report_type == 'simples':
            return SimpleReport.generate(inventory)
        elif report_type == 'completo':
            return CompleteReport.generate(inventory)
        else:
            raise ValueError(f'Unknown report type: {report_type}')

    def __iter__(self):
        return InventoryIterator(self.data)
