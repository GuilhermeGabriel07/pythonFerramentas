import pandas as pd

dados = {
    "Produto": ["Produto A", "Produto B", "Produto C", "Produto D", "Produto E", 
                "Produto F", "Produto G", "Produto H", "Produto I", "Produto J"],
    "Avaliação": [4.5, 3.8, 4.2, 4.7, 3.5, 4.0, 3.9, 4.8, 4.3, 3.7],
    "Quantidade de Vendas": [150, 200, 180, 220, 170, 190, 160, 210, 180, 200]
}
df = pd.DataFrame(dados)
df.to_excel("produtos.xlsx")

print("A planilha foi gerada com sucesso: produtos.xlsx")
