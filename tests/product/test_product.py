from inventory_report.inventory.product import Product


def test_cria_produto():
    produto = Product(
        id=1,
        nome_do_produto="Produto 1",
        nome_da_empresa="Empresa 1",
        data_de_fabricacao="2020-01-01",
        data_de_validade="2020-12-31",
        numero_de_serie=1,
        instrucoes_de_armazenamento="Armazenamento 1",
    )

    assert produto.id == 1
    assert produto.nome_do_produto == "Produto 1"
    assert produto.nome_da_empresa == "Empresa 1"
    assert produto.data_de_fabricacao == "2020-01-01"
    assert produto.data_de_validade == "2020-12-31"
    assert produto.numero_de_serie == 1
    assert produto.instrucoes_de_armazenamento == "Armazenamento 1"

    assert produto.__repr__() == (
        f"O produto {produto.nome_do_produto}"
        f" fabricado em {produto.data_de_fabricacao}"
        f" por {produto.nome_da_empresa} com validade"
        f" até {produto.data_de_validade}"
        f" precisa ser armazenado {produto.instrucoes_de_armazenamento}."
    )
