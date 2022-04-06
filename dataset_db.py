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
    dataset = import_table('dataset', conn)

    # Print the column names
    print(dataset.columns.keys())

    values_list= [{'nome': 'nomeação e classificação prefeitura de maceio e ama v1', 'tipo': 'texto'}]

    insert_db(dataset, conn, values_list)

    query = db.select([dataset])

    ResultProxy = conn.execute(query)
    ResultSet = ResultProxy.fetchall()
    print(ResultSet)
   
if __name__ == '__main__':
    main()