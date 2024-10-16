import streamlit as st
import pandas as pd
import sqlite3

#conectar ao banco de dados:
conn = sqlite3.connect('../data/quotes.db')

#carregar o banco de dados da tabela
df = pd.read_sql_query("SELECT * FROM mercadolivre_items", conn)

#fechar conexão
conn.close()

#titulo
st.title('Pesquisa de mercado - Tenis esportivos')
st.subheader('Principais KPIs')

col1, col2, col3 = st.columns(3)

#numero total de itens:
total_items = df.shape[0]
col1.metric(label="Numero total de Itens", value=total_items)

#Numero total de Itens
unique_brands = df['brand'].nunique()
col2.metric(label="Numero de marcas únicas", value=unique_brands)

#Numero total de Itens
average_new_price = df['new_price'].mean()
col3.metric(label="Preço médio novo R$", value=f"{average_new_price:.2f}")

# Quais marcas são mais encontradas até a 10ª página
st.subheader('Marcas mais encontradas até a 10ª página')
col1, col2 = st.columns([4, 2])
top_10_pages_brands = df['brand'].value_counts().sort_values(ascending=False)
col1.bar_chart(top_10_pages_brands)
col2.write(top_10_pages_brands)

# Qual o preço médio por marca
st.subheader('Preço médio por marca')
col1, col2 = st.columns([4, 2])
df_non_zero_prices = df[df['new_price'] > 0]
average_price_by_brand = df_non_zero_prices.groupby('brand')['new_price'].mean().sort_values(ascending=False)
col1.bar_chart(average_price_by_brand)
col2.write(average_price_by_brand)

# Qual a satisfação por marca
st.subheader('Satisfação por marca')
col1, col2 = st.columns([4, 2])
df_non_zero_reviews = df[df['reviews_rating_number'] > 0]
satisfaction_by_brand = df_non_zero_reviews.groupby('brand')['reviews_rating_number'].mean().sort_values(ascending=False)
col1.bar_chart(satisfaction_by_brand)
col2.write(satisfaction_by_brand)