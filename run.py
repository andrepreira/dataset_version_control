import argparse

from app.datasets.datasets import Datasets
from app.datasets.regex import Regex
from app.experiments.textcat_experiments import TextcatExperiment
from app.training.training import Training

def main():
    dataset_name = 'licitacoes_contratos'
    path_handle = '/home/andre-pereira/projects/aisolutions/dataset_version_control/app/models/event_search_licitacao_contrato.py'
    dataset_name2 = 'vida_funcional'
    path_handle2 = '/home/andre-pereira/projects/aisolutions/dataset_version_control/app/models/event_search_vida_funcional.py'
    
    
    
    # cria dataset
    df = Datasets.execute()
    # regex
    #salva prodigy
    Regex.execute(df, dataset_name)
    
    
    #treina machine learning
    # salva modelo treinado
    
    Training.execute()
    
    # classifica texto
    #salva prodigy
    
    TextcatExperiment.execute()
    #matriz de confusao, score e metricas
    #salva metricas no banco postgres   
    


if __name__ == '__main__':
    main()