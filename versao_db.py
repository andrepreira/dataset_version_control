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

def insert_db(table,conn, value_list):
    query = db.insert(table)
    conn.execute(query, value_list)

def main():
    #Conexão com banco e busca fk
    conn = db_connect()
    id_classificador = busca_fk_id('classificador', conn, 'SGDClassifier')

    versao = import_table('versao', conn)
    values_list= [{
        'nome': 'versão modelo diff 1', 
        'tipo': 'texto', 
        'is_manual': True,
        'descricao': 'diff entre regex e SGDClassifier', 
        'id_classificador': id_classificador
        }]

    insert_db(versao, conn, values_list)
   
if __name__ == '__main__':
    main()