import random
from datetime import datetime, timedelta
from pathlib import Path
import pandas as pd
import names

datasets = Path(__file__).parent / "datasets"
datasets.mkdir(parents=True, exist_ok=True)

STORES = [
    {"estado": "SP", "cidade": "São Paulo", 
     "vendedores": ["Ana Oliveira", "Lucas Pereira"]},
    {"estado": "MG", "cidade": "Belo Horizonte", 
     "vendedores": ["Carlos Silva", "Fernanda Costa"]},
    {"estado": "RJ", "cidade": "Rio de Janeiro", 
     "vendedores": ["Juliana Almeida", "Pedro Souza"]},
    {"estado": "RS", "cidade": "Porto Alegre", 
     "vendedores": ["Mariana Gomes", "Roberto Ferreira"]},
    {"estado": "SC", "cidade": "Florianópolis", 
     "vendedores": ["Gabriela Santos", "Tiago Lima"]},
]

PRODUCTS = [
    {"nome": "Smartphone Samsung Galaxy", "id": 0, "preco": 2500},
    {"nome": "Notebook Dell Inspiron", "id": 1, "preco": 4500},
    {"nome": "Tablet Apple Ipad", "id": 2, "preco": 3000},
    {"nome": "Smartwatch Garmin", "id": 3, "preco": 1200},
    {"nome": "Fone de Ouvido Sony", "id": 4, "preco": 600},
]

PAY_MODE = ["cartão de crédito", "boleto", "pix", "dinheiro"]
GENDER = ["male", "female"]

compras = []

for x in range (2000):
    store = random.choice(STORES)
    seller = random.choice(store["vendedores"])
    product = random.choice(PRODUCTS)
    purchase_time = datetime.now() - timedelta(
        days=random.randint(1, 365),
        hours=random.randint(-5, 5),
        minutes=random.randint(-30, 30)
    )

    client_gender = random.choice(GENDER)
    cliente_name = names.get_full_name(client_gender)
    payment_method = random.choice(PAY_MODE)

    compras.append({
        "Data": purchase_time,
        "Id": 0,
        "Loja": store["cidade"],
        "Vendedor": seller,
        "Produto": product["nome"],
        "Nome do cliente": cliente_name.replace("female", "femenino").replace("male", "masculino"),
        "Fora de pagamento": payment_method
    })

df_compras = pd.DataFrame(compras).set_index("Data").sort_index()
df_compras["Id"] = [x for x in range(len(df_compras))]

df_lojas = pd.DataFrame(STORES)
df_produtos = pd.DataFrame(PRODUCTS)

print(df_lojas)
print(df_compras)
print(df_produtos)

df_compras.to_csv(datasets / "compras.csv", decimal=",", sep=";")
df_produtos.to_csv(datasets / "produtos.csv", decimal=",", sep=";")
df_lojas.to_csv(datasets / "lojas.csv", decimal=",", sep=";")

df_compras.to_excel(datasets / "compras.xlsx")
df_produtos.to_excel(datasets / "produtos.xlsx")
df_lojas.to_excel(datasets / "lojas.xlsx")