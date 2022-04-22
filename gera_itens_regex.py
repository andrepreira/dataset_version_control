import argparse

from database.models import db_connect
from database.seeds.Classificador import Classificador
from database.utils  import *
from classificacao.classificacao_regex import *

def retorna_parametros():
    parser = argparse.ArgumentParser(description='Retorna parâmetros')
    parser.add_argument('-ir', '--id_regex', type=int, 
                    help='insira uma sequencia de ids')
    parser.add_argument('-d', '--dataset_id', type=int,
                    help='insira uma sequencia de ids')
    parser.add_argument('-r', '--rubrix', type=str,
                    help='insira o nome do arquivo rubrix')
    
    args = parser.parse_args()
    return args.id_regex, args.rubrix, args.dataset_id

def main():
    conn = db_connect()
    id_regex,nome_rubrix, dataset_id = retorna_parametros()

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

if __name__ == "__main__":
   main()  