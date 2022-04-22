import argparse

from database.models import db_connect
from database.seeds.Classificador import Classificador
from database.utils  import *
from classificacao.classificacao_ml import *

def retorna_parametros():
    parser = argparse.ArgumentParser(description='Retorna parâmetros')
    parser.add_argument('-i', '--ids', type=int, nargs='+',
                    help='insira uma sequencia de ids')
    parser.add_argument('-d', '--dataset_id', type=int,
                    help='insira uma sequencia de ids')
    parser.add_argument('-r', '--rubrix', type=str,
                    help='insira o nome do arquivo rubrix')
    
    args = parser.parse_args()
    return args.ids, args.rubrix, args.dataset_id

def main():
    conn = db_connect()
    ids,nome_rubrix, dataset_id = retorna_parametros()

    # print(ids[0])
    # print(ids[1])
    # print(ids[2])
    # print(nome_rubrix)
    # print(dataset_id)

    obj = Classificador(dataset_id, conn, nome_rubrix)

    df = select_two_tables(conn, dataset_id)
    
    df, sgd_pipeline = predict_ml(df)
  
    df_erros = obj.extraindo_erros_dataset(df, sgd_pipeline)

    #envio de dados rubrix
    obj.envio_rubrix(df_erros, sgd_pipeline, 'DecisionTreeClassifier')
            
    #machine learning
    obj.insere_labels('classificados', obj.conn, df, ids[0], 'predict_classification', 'dados machine learning salvos no banco!!')

    #diff entre regex e machine learning
    obj.insere_labels('classificados', obj.conn, df_erros, ids[1], 'predict_classification', 'dados diff salvos no banco!!')
    
    print("Finalização do classificador !")

if __name__ == "__main__":
   main()  