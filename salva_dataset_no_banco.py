from sqlalchemy import create_engine
import pandas as pd


def conexao_db():
     return create_engine('postgresql://postgres:postgres@localhost:5432/db_fluxo_mineracao')

def cria_tabela(conn):
    conn.execute("CREATE TABLE IF NOT EXISTS public.backup_dataset (text text NULL, classification varchar(250) NULL, id_texto varchar(100) NULL )")

def insere_dataframe(conn, data):
         data.to_sql('backup_dataset', conn, if_exists='replace', index = False)
def main():

    dataset = pd.read_pickle('./dataset_tratado.pkl')
  
    # Salva dataset no banco de dados
    conn = conexao_db()
    
    cria_tabela(conn)

    insere_dataframe(conn, dataset)
   
if __name__ == '__main__':
    main()