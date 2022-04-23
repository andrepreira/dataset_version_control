import argparse
import glob
import pandas as pd

from database.models import db_connect
from utils import *
from database.utils  import *

def retorna_parametros():
    parser = argparse.ArgumentParser(description='Retorna parâmetros.')
    parser.add_argument('-i', '--ids', type=int, nargs='+',
                    help='insira uma sequencia de ids')
    parser.add_argument('-nd', '--nome_dataset', type=str,
                    help='insira o nome do arquivo rubrix')
    parser.add_argument('-td', '--tipo_dataset', type=str,
                    help='insira o nome do arquivo rubrix')
    
    args = parser.parse_args()
    return args.ids, args.nome_dataset, args.tipo_dataset
   
def get_datas(ano = '2021'):
        ama_datas = glob.glob(f'/home/andre-pereira/projects/data_science/materias/executivo/municipal/ama/edicoes/{ano}/*/*/*.txt')
        maceio_datas = glob.glob(f'/home/andre-pereira/projects/data_science/materias/executivo/municipal/maceio/prefeitura/edicoes/{ano}/*/*/*.txt')

        print(f'the number of txt archive is: {len(ama_datas)}')
        print(f'the number of txt archive is: {len(maceio_datas)}')

        return ama_datas + maceio_datas

def archive_txt_with_path(path):
    file = open(path, "r")
    file = file.read()
    return file    

def dataframe(recived_data):
    if len(recived_data) == 0:
        return 'Your data is empty!'
    datas = pd.DataFrame()
    for path in recived_data:
        file = archive_txt_with_path(path)
#         print(f'path: {path} -  classification: {was_classifield}')
        datas = datas.append({'texto': file}, ignore_index=True)
    
    return datas

#criar itens
def popula_tabela_itens(conn, table_name, id_dataset, dataset):
    # Trata dataset para inserir no banco
    dataset['id_dataset'] = id_dataset
    col = ['texto','id_dataset']
    dataset = dataset[col]

    # Salva dataset no banco de dados
    insere_dataframe_append(table_name, conn, dataset)

def main():
    conn = db_connect()

    ids, nome_dataset, tipo_dataset = retorna_parametros()

    # print(ids[0])
    # print(nome_dataset)
    # print(tipo_dataset)

    # extrai materias
    dataset =  get_datas()
    dataset = dataframe(dataset)

    #cadastra dataset no banco
    values_list_dataset= [{'nome': nome_dataset, 'tipo': tipo_dataset}]
    popula_tabelas_iniciais(conn, 'dataset', values_list_dataset)

    #popula tabela itens
    popula_tabela_itens(conn, 'item', ids[0], dataset)
    print("Fim da geração do dataset !")

if __name__ == '__main__':
    main()
