import argparse

from database.models import db_connect
from utils import *
from database.utils  import *

def retorna_parametros():
    parser = argparse.ArgumentParser(description='Retorna os ids.')
    parser.add_argument('-i', '--ids', type=int, nargs='+',
                    help='insira uma sequencia de ids')
    parser.add_argument('-nv', '--nome_versao', type=str,  nargs='+',
                    help='insira uma sequencia de nome_versao')
    parser.add_argument('-tv', '--tipo_versao', type=str,  nargs='+',
                    help='insira uma sequencia de tipo_versao')
    parser.add_argument('-mv', '--is_manual_versao', type=bool,  nargs='+',
                    help='insira uma sequencia de is_manual_versao')
    parser.add_argument('-dv', '--descricao_versao', type=str,  nargs='+',
                    help='insira uma sequencia de descricao_versao')
    
    args = parser.parse_args()
    return args.ids, args.nome_versao, args.tipo_versao , args.is_manual_versao, args.descricao_versao

def main():
    conn = db_connect()
    ids, nome_versao, tipo_versao, is_manual_versao, descricao_versao = retorna_parametros()

    # print('***values_list_versao***')
    # print(nome_versao[0])
    # print(tipo_versao[0])
    # print(is_manual_versao[0])
    # print(descricao_versao[0])
    # print(ids[0])
    # print(nome_versao[1])
    # print(tipo_versao[1])
    # print(is_manual_versao[1])
    # print(descricao_versao[1])
    # print(ids[1])
    # print(nome_versao[2])
    # print(tipo_versao[2])
    # print(is_manual_versao[2])
    # print(descricao_versao[2])
    # print(ids[2])
    # print(nome_versao[3])
    # print(tipo_versao[3])
    # print(is_manual_versao[3])
    # print(descricao_versao[3])
    # print(ids[3])
    # print(nome_versao[4])
    # print(tipo_versao[4])
    # print(is_manual_versao[4])
    # print(descricao_versao[4])
    # print(ids[4])

    values_list_versao= [{
        'nome': nome_versao[i], 'tipo': tipo_versao[i], 
        'is_manual': is_manual_versao[i], 'descricao': descricao_versao[i], 'id_classificador': ids[i]} for  i in range(len(ids))]

    print(values_list_versao)

    insert_db('versao', conn, values_list_versao)
    print("Fim da geração das versões !")


if __name__ == "__main__":
   main()