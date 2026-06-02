import random
from datetime import datetime, timedelta
from pathlib import Path
import pandas as pd
import names

dataset = Path(__file__).parent / "datasets"
dataset.mkdir(parents=True, exist_ok=True)

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

