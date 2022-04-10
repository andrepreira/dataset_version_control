import sqlalchemy as db

def import_table(table_name, conn):
    metadata = db.MetaData()
    return db.Table(table_name, metadata, autoload=True, autoload_with=conn)

def insert_db(table_name,conn, value_list):
    table = import_table(table_name, conn)
    query = db.insert(table)
    conn.execute(query, value_list)

def insere_dataframe_append(name_table,conn, data):
         data.to_sql(name_table, conn, if_exists='append', index = False)