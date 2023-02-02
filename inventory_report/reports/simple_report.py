from datetime import date
from collections import Counter


class SimpleReport:
    @staticmethod
    def generate(products: list[dict]):
        today = date.today().strftime("%Y/%m/%d")

        oldest_manufacture = min(map(lambda p: (
                p['data_de_fabricacao']
            ), products))

        closest_expiration = min(products, key=lambda p: (
                p['data_de_validade']
                if p['data_de_validade'] < today
                else '9999/99/99'
            ))['data_de_validade']

        company_bigger_stock = Counter(map(lambda p: (
                p['nome_da_empresa']
            ), products)).most_common(1)[0][0]

        return (
            f"Data de fabricação mais antiga: {oldest_manufacture}\n"
            f"Data de validade mais próxima: {closest_expiration}\n"
            f"Empresa com mais produtos: {company_bigger_stock}"
        )
