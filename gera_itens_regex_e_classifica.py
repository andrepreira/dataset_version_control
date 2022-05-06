import argparse
import sys

from database.models import db_connect
from database.seeds.Classificador import Classificador
from database.utils  import *
from utils import *
from classificacao.classificacao_regex import *
from classificacao.classificacao_ml import *

def retorna_parametros():
    parser = argparse.ArgumentParser(description='Retorna parâmetros')
    parser.add_argument('-ir', '--id_regex', type=int, 
                    help='insira uma sequencia de ids')
    parser.add_argument('-d', '--dataset_id', type=int,
                    help='insira uma sequencia de ids')
    parser.add_argument('-r', '--rubrix', type=str,
                    help='insira o nome do arquivo rubrix')
    parser.add_argument('-ivml', '--id_versao_modelo_ml', type=int,
                    help='insira o nome do arquivo rubrix')
    parser.add_argument('-ivdiff', '--id_versao_diff', type=int,
                    help='insira o nome do arquivo rubrix')
    parser.add_argument('-iv', '--versao_id', type=int,
                    help='insira o nome do arquivo rubrix')
    parser.add_argument('-np', '--nome_pipeline', type=str,
                    help='insira o nome do arquivo rubrix')
    parser.add_argument('-nd', '--nome_dataset', type=str,
                    help='insira o nome do arquivo rubrix')
    
    args = parser.parse_args()
    return args.id_regex, args.rubrix, args.dataset_id, args.id_versao_modelo_ml, args.id_versao_diff, args.versao_id, args.nome_pipeline, args.nome_dataset

def main():
    conn = db_connect()
    id_regex,nome_rubrix, dataset_id, id_versao_modelo_ml, id_versao_diff, versao_id, nome_pipeline, nome_dataset = retorna_parametros()

    # print(ids[0])
    # print(ids[1])
    # print(ids[2])
    # print(nome_rubrix)
    # print(dataset_id)

    obj = Classificador(dataset_id, conn, nome_rubrix)
     # pega itens no banco
    item = obj.pega_itens()
    # classifica com regex e retorna dataset com colunas: texto, labels, status
    df = regex(item)
    #regex
    obj.insere_labels('classificados', obj.conn, df,id_regex, 'label_regex', 'dados regex salvos no banco!!')
    print("Finalização dos itens e regex !")
    
    df, sgd_pipeline = predict_regex_ml(df, nome_pipeline, nome_dataset, 'label_regex')
  
    df_erros = obj.extraindo_erros_dataset(df, sgd_pipeline)

    #envio de dados rubrix
    obj.envio_rubrix(df_erros, sgd_pipeline, 'SGDClassifier')
            
    #machine learning
    obj.insere_labels('classificados', obj.conn, df, id_versao_modelo_ml, 'predict_classification', 'dados machine learning salvos no banco!!')

    #diff entre modelos
    obj.insere_labels('classificados', obj.conn, df_erros, id_versao_diff, 'predict_classification', 'dados diff salvos no banco!!')

if __name__ == "__main__":
   main()
   for n in dir():
         if n[0]!='_': delattr(sys.modules[__name__], n)  