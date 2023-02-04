import os
import csv
import json
import xml.etree.ElementTree as ET
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def import_data(path: str, report_type: str):
        _, extension = os.path.splitext(path)

        if extension == ".csv":
            with open(path) as file:
                reader = csv.DictReader(file)
                dicts = [dict(row) for row in reader]
        elif extension == ".json":
            with open(path) as file:
                dicts = json.load(file)
        elif extension == ".xml":
            tree = ET.parse(path)
            root = tree.getroot()
            dicts = []
            for record in root.findall('record'):
                record_dict = {}
                for item in record:
                    record_dict[item.tag] = item.text
                dicts.append(record_dict)

        if report_type == 'simples':
            return SimpleReport.generate(list(dicts))
        elif report_type == 'completo':
            return CompleteReport.generate(list(dicts))
        else:
            raise ValueError(f'Unknown report type: {report_type}')
