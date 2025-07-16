#importar bibliotecas necessárias
import pandas as pd
import sqlite3 
from datetime import datetime

#definir rota pro arquivo jsonl
df = pd.read_json('../data/data.json', lines=True)

#SÓ PRA EXIBIR TODAS AS COLUNAS NO TERMINAL
pd.options.display.max_columns = None

#adiconar coluna source com um valor fixo
df['_source'] = "https://lista.mercadolivre.com.br/tenis-de-corrida-masculino"

#adicionar coluna com a data da coleta e hora
df['_data_coleta'] = datetime.now()

#Tratar valores nulos para colunas numericas e de texto
df['old_price_reais'] = df['old_price_reais'].fillna(0).astype(float)
df['old_price_centavos'] = df['old_price_centavos'].fillna(0).astype(float)
df['new_price_reais'] = df['new_price_reais'].fillna(0).astype(float)
df['new_price_centavos'] = df['new_price_centavos'].fillna(0).astype(float)
df['reviews_rating_number'] = df['reviews_rating_number'].fillna(0).astype(float)

#remover os parenteses do reviews_amount
df['reviews_amount'] = df['reviews_amount'].str.replace('[\\(\\)]', '', regex=True)

df['reviews_amount'] = df['reviews_amount'].fillna(0).astype(int)



# Tratar os preços como floats e calcular os valores totais
df['old_price'] = df['old_price_reais'] + df['old_price_centavos'] / 100
df['new_price'] = df['new_price_reais'] + df['new_price_centavos'] / 100

# Remover as colunas antigas de preços
df.drop(columns=['old_price_reais', 'old_price_centavos', 'new_price_reais', 'new_price_centavos'], inplace=True)

print(df.head())
""""
# Conectar ao banco de dados SQLite (ou criar um novo)
conn = sqlite3.connect('../data/quotes.db')

# Salvar o DataFrame no banco de dados SQLite
df.to_sql('mercadolivre_items', conn, if_exists='replace', index=False)

# Fechar a conexão com o banco de dados
conn.close()
"""