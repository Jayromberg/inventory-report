from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(products: list[dict]):
        simple_report = SimpleReport.generate(products)

        stock_by_company = Counter(map(lambda p: (
            p['nome_da_empresa']
        ), products)).most_common()

        # company = '\n'.join(map(lambda c: (
        #     f'- {c[0]}: {c[1]}'
        #     ), stock_by_company))

        companies_and_stocks = ''

        for company, stock in stock_by_company:
            companies_and_stocks += f"- {company}: {stock}\n"

        return (
            f"{simple_report}\n"
            "Produtos estocados por empresa:\n"
            f"{companies_and_stocks}"
        )
