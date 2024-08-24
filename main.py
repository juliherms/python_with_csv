from etl import ler_csv, filrar_produtos_nao_entregues, somar_valores_dos_produtos

path_arquivo = "vendas.csv"

lista_de_produtos = ler_csv(path_arquivo)
produtos_entegues = filrar_produtos_nao_entregues(lista_de_produtos)
valor_dos_produtos_entregues = somar_valores_dos_produtos(produtos_entegues)
print(produtos_entegues)
print(valor_dos_produtos_entregues)