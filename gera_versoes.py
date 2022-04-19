from database.models import db_connect
from utils import *
from database.utils  import *

def main():
    conn = db_connect()

    values_list_classificador= [{'nome':'EventSearch',
        'tipo':'regex',
        'path': '/home/andre-pereira/projects/data_science/aisolutions/fluxo_mineracao/classificacao/EventSearch.py'},
    { 'nome': 'SGDClassifier', 
        'tipo': 'classificador sklearn',
        'path': '/home/andre-pereira/projects/data_science/aisolutions/fluxo_mineracao/sgd_pipeline.pkl'}]

    popula_tabelas_iniciais(conn, 'classificador', values_list_classificador)

    values_list_versao= [{
            'nome': 'versão regex v1', 
            'tipo': 'texto', 
            'is_manual': False,
            'descricao': 'classificação fraca com regex versao v1', 
            'id_classificador': 1
            },{
            'nome': 'versao modelo SGD v1', 
            'tipo': 'texto', 
            'is_manual': False,
            'descricao': 'classificação com SGDClassifier v1', 
            'id_classificador': 2
            },{
            'nome': 'versão modelo diff v1', 
            'tipo': 'texto', 
            'is_manual': False,
            'descricao': 'diff entre regex e SGDClassifier', 
            'id_classificador': 2
            },{
            'nome': 'versao rubrix v1', 
            'tipo': 'texto', 
            'is_manual': True,
            'descricao': 'correção feita manualmente usando o rubrix', 
            'id_classificador': 2
            },{
            'nome': 'versao merge modelo SGD v1 e rubrix v1', 
            'tipo': 'texto', 
            'is_manual': False,
            'descricao': 'dataset corrigido com a classificação manual  rubrix v1', 
            'id_classificador': 2
            }]

    insert_db('versao', conn, values_list_versao)
    print("Fim da geração das versões !")


if __name__ == "__main__":
   main()