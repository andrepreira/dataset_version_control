from database.models import db_connect
import utils
import sqlalchemy as db
import pandas as pd

def import_table(table_name, conn):
    metadata = db.MetaData()
    return db.Table(table_name, metadata, autoload=True, autoload_with=conn)

def busca_fk_id(table_name, conn, nome):
    table = import_table(table_name, conn)
    query = db.select([table.columns.id]).where(table.columns.nome == nome)
    id =  conn.execute(query).fetchall()
    return  id[0][0]

def busca_fk_id_item(table_name, conn, nome):
    table = import_table(table_name, conn)
    query = db.select([table.columns.id_dataset]).where(table.columns.nome == nome)
    id =  conn.execute(query).fetchall()
    return  id[0][0]

def insert_db(table,conn, value_list):
    query = db.insert(table)
    conn.execute(query, value_list)

def insere_dataframe_append(name_table,conn, data):
         data.to_sql(name_table, conn, if_exists='append', index = False)

def main():
    #Conexão com banco e busca fk
    conn = db_connect()

    id_item = busca_fk_id_item('item', conn,  'nomeação e classificação')
    id_versao = busca_fk_id('versao', conn,  'versão modelo SGD 1')

    # Trata dataset para inserir no banco
    dataset = utils.read_dataset_pkl('dataset_treinado')
    dataset['id_item'] = id_item
    dataset['id_versao'] = id_versao
    dataset = dataset.rename(columns = {'predict_classification': 'label'})
    col = ['label','id_item', 'id_versao']
    dataset = dataset[col]

    # Salva dataset no banco de dados
    insere_dataframe_append('classificados', conn, dataset)
   
if __name__ == '__main__':
    main()