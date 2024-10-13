#importar bibliotecas necessárias
import pandas as pd
import sqlite3 
import datetime

#definir rota pro arquivo json
df = pd.read_json('../data/data.jsonl', lines=True)
print(df)