import glob
import pandas as pd

def get_datas(ano = '2021'):
        ama_datas = glob.glob(f'/var/projects/tceal/materias/executivo/municipal/ama/edicoes/{ano}/*/*/*.txt')
        maceio_datas = glob.glob(f'/var/projects/tceal/materias/executivo/municipal/maceio/prefeitura/edicoes/{ano}/*/*/*.txt')

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

def main():

    dataset =  get_datas()

    dataset = dataframe(dataset)

    dataset.to_pickle("./dataset_2021.pkl")

if __name__ == '__main__':
    main()