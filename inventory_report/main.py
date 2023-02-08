import os
import sys
from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


def main():
    if len(sys.argv) < 3:
        return print("Verifique os argumentos", file=sys.stderr)

    path = sys.argv[1]
    report_type = sys.argv[2]

    _, extension = os.path.splitext(path)

    if extension == '.csv':
        inventory_refactor = InventoryRefactor(CsvImporter)
        inventory = inventory_refactor.import_data(path, report_type)
        sys.stdout.write(inventory)
    elif extension == '.json':
        inventory_refactor = InventoryRefactor(JsonImporter)
        inventory = inventory_refactor.import_data(path, report_type)
        sys.stdout.write(inventory)
    elif extension == '.xml':
        inventory_refactor = InventoryRefactor(XmlImporter)
        inventory = inventory_refactor.import_data(path, report_type)
        sys.stdout.write(inventory)
    else:
        return print("Arquivo inválido", file=sys.stderr)
