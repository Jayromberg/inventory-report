from inventory_report.inventory.product import Product


def test_relatorio_produto():
    p = Product(
        id=1,
        nome_do_produto="Produto 1",
        nome_da_empresa="Empresa 1",
        data_de_fabricacao="2020-01-01",
        data_de_validade="2020-01-02",
        numero_de_serie=1,
        instrucoes_de_armazenamento="Armazenamento 1",
    )
    assert p.__repr__() == (
        f"O produto {p.nome_do_produto}"
        f" fabricado em {p.data_de_fabricacao}"
        f" por {p.nome_da_empresa} com validade"
        f" até {p.data_de_validade}"
        f" precisa ser armazenado {p.instrucoes_de_armazenamento}."
    )
