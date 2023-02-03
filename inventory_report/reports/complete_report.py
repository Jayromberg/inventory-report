from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(products: list[dict]):
        simple_report = SimpleReport.generate(products)

        stock_by_company = Counter(map(lambda p: (
            p['nome_da_empresa']
        ), products)).most_common()

        companies = []

        for company, stock in stock_by_company:
            companies.append(f"- {company}: {stock}")

        return (
            f"{simple_report}\n"
            "Produtos estocados por empresa:\n"
            f"{companies[0]}\n"
            f"{companies[1]}\n"
            f"{companies[2]}\n"
        )
