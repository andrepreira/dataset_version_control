import argparse
from ast import arg

from database.models import db_connect
from utils import *
from database.utils  import *

def retorna_parametros():
    parser = argparse.ArgumentParser(description='Retorna os ids.')
    parser.add_argument('-i', '--ids', type=int, nargs='+',
                    help='insira uma sequencia de ids')
    parser.add_argument('-nc', '--nome_classificador', type=str,  nargs='+',
                    help='insira uma sequencia de nome_classificador')
    parser.add_argument('-tc', '--tipo_classificador', type=str,  nargs='+',
                    help='insira uma sequencia de tipo_classificador')
    parser.add_argument('-pc', '--path_classificador', type=str,  nargs='+',
                    help='insira uma sequencia de path_classificador')
    parser.add_argument('-nv', '--nome_versao', type=str,  nargs='+',
                    help='insira uma sequencia de nome_versao')
    parser.add_argument('-tv', '--tipo_versao', type=str,  nargs='+',
                    help='insira uma sequencia de tipo_versao')
    parser.add_argument('-mv', '--is_manual_versao', type=bool,  nargs='+',
                    help='insira uma sequencia de is_manual_versao')
    parser.add_argument('-dv', '--descricao_versao', type=str,  nargs='+',
                    help='insira uma sequencia de descricao_versao')
    
    args = parser.parse_args()
    return args.ids, args.nome_classificador,args.tipo_classificador, args.path_classificador, args.nome_versao, args.tipo_versao , args.is_manual_versao, args.descricao_versao

def main():
    conn = db_connect()
    ids, nome_classificador, tipo_classificador, path_classificador, nome_versao, tipo_versao, is_manual_versao, descricao_versao = retorna_parametros()
    print('***values_list_classificador***')
    print(nome_classificador[0])
    print(tipo_classificador[0])
    print(path_classificador[0])
    print(nome_classificador[1])
    print(tipo_classificador[1])
    print(path_classificador[1])

    print('***values_list_versao***')
    print(nome_versao[0])
    print(tipo_versao[0])
    print(is_manual_versao[0])
    print(descricao_versao[0])
    print(ids[0])
    print(nome_versao[1])
    print(tipo_versao[1])
    print(is_manual_versao[1])
    print(descricao_versao[1])
    print(ids[1])
    print(nome_versao[2])
    print(tipo_versao[2])
    print(is_manual_versao[2])
    print(descricao_versao[2])
    print(ids[2])
    print(nome_versao[3])
    print(tipo_versao[3])
    print(is_manual_versao[3])
    print(descricao_versao[3])
    print(ids[3])
    print(nome_versao[4])
    print(tipo_versao[4])
    print(is_manual_versao[4])
    print(descricao_versao[4])
    print(ids[4])

    # values_list_classificador= [{'nome': nome_classificador[0],
    #     'tipo':tipo_classificador[0],
    #     'path': path_classificador[0]},
    # { 'nome': nome_classificador[1], 
    #     'tipo': tipo_classificador[1],
    #     'path': path_classificador[1]}]

    # popula_tabelas_iniciais(conn, 'classificador', values_list_classificador)

    # values_list_versao= [{
    #         'nome': 'versão regex v1', 
    #         'tipo': 'texto', 
    #         'is_manual': False,
    #         'descricao': 'classificação fraca com regex versao v1', 
    #         'id_classificador': ids[0]
    #         },{
    #         'nome': 'versao modelo SGD v1', 
    #         'tipo': 'texto', 
    #         'is_manual': False,
    #         'descricao': 'classificação com SGDClassifier v1', 
    #         'id_classificador': ids[1]
    #         },{
    #         'nome': 'versão modelo diff v1', 
    #         'tipo': 'texto', 
    #         'is_manual': False,
    #         'descricao': 'diff entre regex e SGDClassifier', 
    #         'id_classificador': ids[2]
    #         },{
    #         'nome': 'versao rubrix v1', 
    #         'tipo': 'texto', 
    #         'is_manual': True,
    #         'descricao': 'correção feita manualmente usando o rubrix', 
    #         'id_classificador': ids[3]
    #         },{
    #         'nome': 'versao merge modelo SGD v1 e rubrix v1', 
    #         'tipo': 'texto', 
    #         'is_manual': False,
    #         'descricao': 'dataset corrigido com a classificação manual  rubrix v1', 
    #         'id_classificador': ids[4]
    #         }]

    # insert_db('versao', conn, values_list_versao)
    # print("Fim da geração das versões !")


if __name__ == "__main__":
   main()