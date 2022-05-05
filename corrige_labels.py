import argparse
import rubrix as rb

from database.models import db_connect
from database.seeds.Classificador import Classificador
from database.utils  import *

def retorna_parametros():
    parser = argparse.ArgumentParser(description='Retorna os ids.')
    parser.add_argument('-ivr', '--id_version_rubrix', type=int,
                    help='insira o nome do arquivo rubrix')
    parser.add_argument('-ivml', '--id_version_modelo_ml', type=int,
                    help='insira o nome do arquivo rubrix')
    parser.add_argument('-ivm', '--id_version_merge', type=int,
                    help='insira o nome do arquivo rubrix')
    parser.add_argument('-d', '--dataset_id', type=int,
                    help='insira uma sequencia de ids')
    parser.add_argument('-r', '--rubrix', type=str,
                    help='insira o nome do arquivo rubrix')
    
    args = parser.parse_args()
    return args.id_version_rubrix, args.id_version_modelo_ml, args.id_version_merge, args.dataset_id, args.rubrix

def salva_merge(df, label_name, conn, id_versao, msg='dados salvos'):
    for idx, row in df.iterrows():
        value = [{'label': row[label_name], 'id_item': row['id_item'], 'id_versao': id_versao}]
        # print(value)
        insert_db('classificados', conn, value)
    
    print(msg)

def load_df_rubrix(nome_rubrix):
     rb.init(api_url="http://localhost:6900")

     df = rb.load(nome_rubrix)

     df  = extrai_inputs_rubrix(df)

     return df

def insere_labels(name_table,conn, data, id_versao, label_name='label', msg='dados salvos'):
        data = insere_id_versao(data, id_versao)
        data = data.rename(columns = {label_name: 'label'})
        data.to_sql(name_table, conn, if_exists='append', index = False)
        print(msg)

def merge_dataset(df, df2):
    # listas de id's
    lists_id = [idx for idx in df2.id_item]
    df[f'merge_label'] = df[f'label']
  
    print(len(df))
    for idx, row in df.iterrows():
        id_item = row['id_item']
        if id_item in lists_id:
            df.loc[df.id_item == id_item, f'merge_label'] = df2['label'][df2.id_item == id_item].values[0]
    print(len(df))
    filtra = list(df2.id_item.apply(int))
    print(df.query('id_item in @filtra').head(30))
    col = ['merge_label', 'id_item']
    df = df[col]
    df = df.rename(columns = {'merge_label': 'label'})
    return df

def insere_id_versao(df, id_versao):
    df['id_versao'] = id_versao
    return df

def extrai_inputs_rubrix(df_rubrix):
    df = None
    df = pd.DataFrame()
    for t, row in df_rubrix.iterrows():
        df = df.append({'id_item': int(float(row['inputs']['id'])), 'label': row['annotation'], 'texto': row['inputs']['texto']}, ignore_index=True)
#     print(row['id'], row['annotation'], row['inputs']['text'])
    # df.to_pickle(f'./versiona_vida_funcional_sgd/dataset/df_correcao_rubrix_v{n_versao}.pkl')
    df.id_item = df.id_item.apply(int)
    col = ['label', 'id_item']
    df = df[col]
    return df

def main():
   
    conn = db_connect()
    id_version_rubrix, id_version_modelo_ml, id_version_merge, dataset_id, nome_rubrix = retorna_parametros()

    c = Classificador(dataset_id, conn, nome_rubrix)

    df_corrigido = load_df_rubrix(nome_rubrix)

    #pega labels machine learning no banco
    df_modelo = select_labels('classificados', conn, id_version_modelo_ml)
    df = merge_dataset(df_modelo, df_corrigido)

    #salva labels classificadas manualmente no rubrix
    insere_labels('classificados', conn, df_corrigido, id_version_rubrix, msg='dados rubrix salvos no banco!!')

    #merge das labels preditas pelo modelo e corrigidas manualmente no rubrix
    insere_labels('classificados', conn, df, id_version_merge, msg='dados merge salvos no banco!!')

if __name__ == "__main__":
   main()  
