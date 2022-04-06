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

def insere_dataframe_append(name_table,conn, data):
         data.to_sql(name_table, conn, if_exists='append', index = False)

def main():
    #Conexão com banco e busca fk
    conn = db_connect()
    id_dataset = busca_fk_id('dataset', conn, 'nomeação e classificação prefeitura de maceio e ama v1')

    # Trata dataset para inserir no banco
    dataset = utils.read_dataset_pkl('dataset_treinado')
    dataset['id_dataset'] = id_dataset
    dataset = dataset.rename(columns = {'text': 'texto'})
    col = ['texto','id_dataset']
    dataset = dataset[col]

    # Salva dataset no banco de dados
    insere_dataframe_append('item', conn, dataset)

    # Print id_dataset
    print(id_dataset)
   
if __name__ == '__main__':
    main()