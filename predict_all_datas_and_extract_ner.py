import argparse
import pandas as pd
import joblib
import spacy

from utils import *
from database.utils  import *
from database.models import db_connect

def retorna_parametros():
    parser = argparse.ArgumentParser(description='Retorna parâmetros.')
    parser.add_argument('-idv', '--dataset_id', type=int,
                    help='retorna id do dataset')
    parser.add_argument('-idv', '--id_versao', type=int,
                    help='insira uma sequencia de ids')
    args = parser.parse_args()
    return args.dataset_id, args.id_versao

def predict_all_datas_ml(df, pipeline):

    y_pred_all = pipeline.predict(df.texto)
    df['predict_classification'] = y_pred_all

    y_pred_proba_all = pipeline.predict_proba(df.texto)

    df['predict_proba_label'] = list(y_pred_proba_all)

    df.to_pickle('./predict_all_datas_ml.pkl')
    return df

def extrai_entidades_nomeadas(dataset, id_versao):
    datas = pd.DataFrame()
    nlp = spacy.load('pt_core_news_sm')
    for idx, row in dataset.iterrows():
        doc = nlp(row['texto'])
        for ent in doc.ents:
            datas = datas.append({'entidade': ent.text, 'tipo': ent.label_, 
                            'start_char': ent.start_char, 'end_char': ent.end_char, 
                            'id_item': row['id_item'], 'id_versao': id_versao, 'label': row['predict_classification']}, ignore_index=True)
    return datas

def select_all_itens(conn, id_dataset):
    item = import_table('item', conn)
    classificados = import_table('classificados', conn)

    query = db.select([item.columns.texto, classificados.columns.id_item]).where(db.and_(item.columns.id == classificados.columns.id_item,
     item.columns.id_dataset == id_dataset, classificados.columns.id_versao == 1))

    r =  conn.execute(query).fetchall()
    df = pd.DataFrame(r)
    df.columns = r[0].keys()
    return  df

def main():
    conn = db_connect()
    dataset_id, id_versao = retorna_parametros()
    sgd_pipeline = joblib.load('./notebook/versiona_vida_funcional_sgd/pipeline/sgd_pipeline_v5.pkl')
    
    df = select_all_itens(conn, dataset_id)
    df = predict_all_datas_ml(df, sgd_pipeline)

    lista = [
        'NOMEACAO DE CARGO EM COMISSAO',
        'EXONERACAO DE CARGO EFETIVO', 
        'EXONERACAO DE CARGO EM COMISSAO', 
        'NOMEACAO EM CARGO EFETIVO',
        'DEMISSAO',
        'APOSENTADORIA'
        ]

    datas = df.query("predict_classification in @lista")
    
    datas = extrai_entidades_nomeadas(datas, id_versao)
    print(datas)
    insere_dataframe_append('entidades', conn, datas)
if __name__ == "__main__":
   main()  