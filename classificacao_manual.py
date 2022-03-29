from sqlalchemy import create_engine
import pandas as pd
import utils
import rubrix as rb

rb.init(api_url="http://localhost:6900")

from database.models import db_connect
from dataset import erros, erros_prob
from enviar_dados_rubrix import DATASET_ERROS_RUBRIX

def insere_dataframe_append(name_table,conn, data):
         data.to_sql(name_table, conn, if_exists='append', index = True, index_label = 'id_classificacao_manual')
def trata_dataset_classificacao_manual_rubrix(dataset):
        col = ['annotation', 'id_texto','annotation_agent', 'prediction','prediction_agent']
        dataset['text'] = [dataset.inputs[i]['text'] for i in range(dataset.inputs.shape[0])]
        dataset = utils.extrair_id_texto(dataset)
        return dataset[col]

def main():
    conn = db_connect()

    dataset_classificacao_manual = rb.load(DATASET_ERROS_RUBRIX)

    dataset_classificacao_manual = trata_dataset_classificacao_manual_rubrix(dataset_classificacao_manual)

    # Salva dataset no banco de dados
    insere_dataframe_append('classificacao_manual', conn, dataset_classificacao_manual)
   
if __name__ == '__main__':
    main()