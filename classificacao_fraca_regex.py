import pandas as pd
import utils

from database.models import db_connect

def insere_dataframe_append(name_table,conn, data):
         data.to_sql(name_table, conn, if_exists='append', index = True, index_label = 'id_classificacao_fraca_regex')
def main():
    conn = db_connect()

    dataset = utils.read_dataset_pkl('dataset_tratado')
    col = ['classification', 'id_texto']
    dataset = dataset[col]

    # Salva dataset no banco de dados
    insere_dataframe_append('classificacao_fraca_regex', conn, dataset)
   
if __name__ == '__main__':
    main()