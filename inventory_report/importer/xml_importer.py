import os
import xml.etree.ElementTree as ET
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @staticmethod
    def import_data(path: str):
        _, extension = os.path.splitext(path)

        if extension != '.xml':
            raise ValueError("Arquivo inválido")

        tree = ET.parse(path)
        root = tree.getroot()
        dicts = []
        for record in root.findall('record'):
            record_dict = {}
            for item in record:
                record_dict[item.tag] = item.text
            dicts.append(record_dict)

        return dicts
