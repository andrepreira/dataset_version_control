import argparse

from database.models import db_connect
from utils import *
from database.utils  import *

def retorna_parametros():
    parser = argparse.ArgumentParser(description='Retorna os ids.')
    parser.add_argument('-nc', '--nome_classificador', type=str,  nargs='+',
                    help='insira uma sequencia de nome_classificador')
    parser.add_argument('-tc', '--tipo_classificador', type=str,  nargs='+',
                    help='insira uma sequencia de tipo_classificador')
    parser.add_argument('-pc', '--path_classificador', type=str,  nargs='+',
                    help='insira uma sequencia de path_classificador')
    
    args = parser.parse_args()
    return args.nome_classificador,args.tipo_classificador, args.path_classificador

def main():
    conn = db_connect()
    nome_classificador, tipo_classificador, path_classificador = retorna_parametros()

    # print('***values_list_classificador***')
    # print(nome_classificador[0])
    # print(tipo_classificador[0])
    # print(path_classificador[0])
    # print(nome_classificador[1])
    # print(tipo_classificador[1])
    # print(path_classificador[1])

    values_list_classificador= [{'nome': nome_classificador[i],
        'tipo':tipo_classificador[i],
        'path': path_classificador[i]} for  i in range(len(nome_classificador)) if nome_classificador[0]]

    popula_tabelas_iniciais(conn, 'classificador', values_list_classificador)

    print(values_list_classificador)

    print("Fim da geração dos classificadores !")

if __name__ == "__main__":
   main()