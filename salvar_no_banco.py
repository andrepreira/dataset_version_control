from utils import extrair_id_texto, substitui_textos_classificados
import dataset as data

import rubrix as rb
import pandas as pd

# Recebe dados classificados do rubrix e salva do banco de dados

df_erros = rb.load('teste_erros_tf-idf')
df_erros.head(1)

# #retira textos não classificados

# print(len(df_erros))
# df_erros = df_erros.dropna(subset=['annotation'])
# df_erros = df_erros.reset_index()
# print(len(df_erros))

df_erros['text'] = [df_erros.inputs[i]['text'] for i in range(df_erros.inputs.shape[0])]
df_erros = extrair_id_texto(df_erros)
df_erros = df_erros.rename(columns = {'annotation': 'classification'})

col = ['text', 'classification', 'id_texto']
df_erros = df_erros[col]

print(df_erros.groupby(['classification']).size())
print(len(df_erros))
df_erros.head(1)

from sqlalchemy import create_engine
engine = create_engine('postgresql://postgres:postgres@localhost:5432/postgres')

engine.execute("CREATE TABLE IF NOT EXISTS public.fluxo_mineracao (text text NULL, classification varchar(250) NULL, id_texto varchar(100) NULL )")

df_erros.to_sql('fluxo_mineracao', engine, if_exists='replace', index = False)

df_erros = pd.read_sql('SELECT text, classification, id_texto FROM fluxo_mineracao', engine)
df_erros.head(1)

data.dataset.groupby(['classification']).size()

dataset = substitui_textos_classificados(data.dataset, df_erros)

dataset.groupby(['classification']).size()

def main():
  
  
if __name__ == '__main__':
    main()