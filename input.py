import pandas as pd

from database.models import db_connect
import utils

def insere_dataframe_replace(name_table,conn, data):
         data.to_sql(name_table, conn, if_exists='replace', index = True, index_label = 'id_input')
def main():
    conn = db_connect()

    dataset = utils.read_dataset_pkl('dataset_treinado')
    col = ['text','id_texto']
    dataset = dataset[col]

    # Salva dataset no banco de dados
    insere_dataframe_replace('input', conn, dataset)
   
if __name__ == '__main__':
    main()