import pandas as pd
import sqlite3

excel_file = "Netflix Dataset Latest 2021.xlsx"
data = pd.read_excel(excel_file)

db_connection = sqlite3.connect("netflix_db.sqlite")

data.to_sql("netflix_data", db_connection, if_exists="replace", index=False)

db_connection.close()

print("Banco de Dados criadocom sucesso!")
