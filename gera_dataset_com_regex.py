import glob
import re
import pandas as pd

from utils import data_classification

def get_datas(ano = '2021'):
        ama_datas = glob.glob(f'/var/projects/tceal/materias/executivo/municipal/ama/edicoes/{ano}/*/*/*.txt')
        maceio_datas = glob.glob(f'/var/projects/tceal/materias/executivo/municipal/maceio/prefeitura/edicoes/{ano}/*/*/*.txt')

        print(f'the number of txt archive is: {len(ama_datas)}')
        print(f'the number of txt archive is: {len(maceio_datas)}')

        return ama_datas + maceio_datas

def main():

    dataset =  get_datas()

    dataset = data_classification(dataset)

    dataset.to_pickle("./dataset_2021.pkl")

if __name__ == '__main__':
    main()