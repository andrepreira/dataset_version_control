import argparse
import rubrix as rb

from database.models import db_connect
from database.seeds.Classificador import Classificador
from database.utils  import *

def retorna_parametros():
    parser = argparse.ArgumentParser(description='Retorna os ids.')
    parser.add_argument('-i', '--ids', type=int, nargs='+',
                    help='insira uma sequencia de ids')
    parser.add_argument('-r', '--rubrix', type=str,
                    help='insira o nome do arquivo rubrix')
    
    args = parser.parse_args()
    return args.ids, args.rubrix

def salva_merge(df, label_name, conn, id_versao, msg='dados salvos'):
    for idx, row in df.iterrows():
        value = [{'label': row[label_name], 'id_item': row['id_item'], 'id_versao': id_versao}]
        # print(value)
        insert_db('classificados', conn, value)
    
    print(msg)

def trata_df_rubrix(df):
    # id_item dos dados classificados manualmente
    df['id_item'] = df.id.apply(lambda x: x+1)
    df = df.rename(columns = {'annotation': 'label'})
    col = ['label', 'id_item']
    df = df[col]
    return df

def load_df_rubrix(nome_rubrix):
     rb.init(api_url="http://localhost:6900")

     df = rb.load(nome_rubrix)

     df = trata_df_rubrix(df)

     return df

def insere_labels(name_table,conn, data, id_versao, label_name='label', msg='dados salvos'):
        data = insere_id_versao(data, id_versao)
        data = data.rename(columns = {label_name: 'label'})
        data.to_sql(name_table, conn, if_exists='append', index = False)
        print(msg)

def substitui_labels_corrigidas(df_antigo, df_corrigido):
    # labels corrigidas
    lists_id_item = [idxx for idxx in df_corrigido.id_item]

    # excluir labels antigas
    print(len(df_antigo))
    for idx, row in df_antigo.iterrows():
        id_item = row['id_item']
        if id_item in lists_id_item:
            df_antigo =  df_antigo.drop([idx])
    print(len(df_antigo))

    #substitui labels antigas pelas corrigidas
    dfs = [df_antigo, df_corrigido]
    df_antigo = pd.concat(dfs)

    return df_antigo

def insere_id_versao(df, id_versao):
    df['id_versao'] = id_versao
    return df

def main():
   
    conn = db_connect()
    ids, nome_rubrix = retorna_parametros()
    print(ids[0])
    print(ids[1])
    print(ids[2])
    print(ids[3])
    print(nome_rubrix)

    # c = Classificador(ids[0], conn)

    # df_corrigido = load_df_rubrix(nome_rubrix)

    # #salva labels classificadas manualmente no rubrix
    # insere_labels('classificados', conn, df_corrigido, ids[1], msg='dados rubrix salvos no banco!!')

    # #pega labels machine learning no banco
    # df_modelo = select_labels('classificados', conn, ids[2])
    # df = substitui_labels_corrigidas(df_modelo, df_corrigido)

    # #merge das labels preditas pelo modelo e corrigidas manualmente no rubrix
    # insere_labels('classificados', conn, df, ids[3], msg='dados merge salvos no banco!!')

if __name__ == "__main__":
   main()  
