from database.models import db_connect
import utils
import sqlalchemy as db

def import_table(table_name, conn):
    metadata = db.MetaData()
    return db.Table(table_name, metadata, autoload=True, autoload_with=conn)

def insert_db(table,conn, value_list):
    query = db.insert(table)
    conn.execute(query, value_list)

def main():
    conn = db_connect()
    classificador = import_table('classificador', conn)

    # Print the column names
    print(classificador.columns.keys())

    values_list= [{'nome': 'SGDClassifier', 'path': '/home/andre-pereira/projects/data_science/aisolutions/fluxo_mineracao/sgd_pipeline.pkl'}]

    insert_db(classificador, conn, values_list)

    query = db.select([classificador])

    ResultProxy = conn.execute(query)
    ResultSet = ResultProxy.fetchall()
    print(ResultSet)
   
if __name__ == '__main__':
    main()