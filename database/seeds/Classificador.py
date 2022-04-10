from database.utils  import *
import pandas as pd
from classificacao.classificacao_ml import *
from classificacao.classificacao_regex import *

class Classificador:
    
    def __init__(self, id_dataset, conn):
        self.id_dataset = id_dataset
        self.conn = conn
    
    def pega_itens(self):
        item = import_table('item', self.conn)
        query = db.select([item.columns.id,item.columns.texto]).where(item.columns.id_dataset == self.id_dataset)
        r = self.conn.execute(query).fetchall()
        df = pd.DataFrame(r)
        df.columns = r[0].keys()
        return df
    
    def salva_na_tabela_classificados(self, df, label_name, id_versao, msg='dados salvos'):
        for idx, row in df.iterrows():
            value = [{'label': row[label_name], 'id_item': row['id'], 'id_versao': id_versao}]
            insert_db('classificados', self.conn, value)
        
        print(msg)

    def run(self):
        # pega itens no banco
        item = self.pega_itens()
        # classifica com regex e retorna dataset com colunas: texto, labels, status
        df = regex(item)
        df = extract_label(df)

        #regex
        self.salva_na_tabela_classificados(df,'label_regex',1,'dados regex salvos no banco!!')
                
        #machine learning
        self.salva_na_tabela_classificados(df,'predict_classification',2,'dados machine learning salvos no banco!!')
        
        # labels_erros = extract_label_erros()
