import argparse

from database.models import db_connect
from database.seeds.Classificador import Classificador
from database.utils  import *

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
    print(ids[0])
    print(ids[1])
    print(ids[2])
    print(nome_rubrix)
    print(dataset_id)
    # obj = Classificador(dataset_id, conn, nome_rubrix, ids)
    # obj.run()
    # print("Finalização do classificador !")

if __name__ == "__main__":
   main()  