import pandas as pd

from database.models import db_connect
import utils

def insere_dataframe_append(name_table,conn, data):
         data.to_sql(name_table, conn, if_exists='append', index = True, index_label = 'id_classificacao_modelo')
def main():
    conn = db_connect()

    dataset = utils.read_dataset_pkl('dataset_treinado')
    col = ['predict_classification', 'id_texto']
    dataset = dataset[col]

    # Salva dataset no banco de dados
    insere_dataframe_append('classificacao_modelo', conn, dataset)
   
if __name__ == '__main__':
    main()