# %matplotlib inline
import matplotlib.pyplot as plt

import pandas as pd
import glob
import re

from classificacao.EventSearch import EventSearcher as event

# extrair id_texto
def extrair_id_texto(df2):
    #EXTRAIR ID TEXTO
    regex_id_texto = re.compile(r'(Codigo Identificador:)([A-Za-z\s?\d?]*)')
    regex_limpar = re.compile(r'Codigo Identificador:')
    regex_quebra_de_linha = re.compile(r'(\n)')

    def cortar_cargo_no_texto(text):
        m = regex_id_texto.search(text)
        if m:
            m = m.group()
            return m
        else:
            return '-'

    def limpar_texto(text):
        n = regex_limpar.sub('',text)
        return n

    id_textos = []
    for idx, row in df2.iterrows():
        text = row['text']
        id_texto = cortar_cargo_no_texto(text)
        id_texto = limpar_texto(id_texto)

        id_textos.append(id_texto)
    len(id_textos)


    df2.insert(4, 'id_texto',id_textos ,allow_duplicates=False)
    return df2

# verifica textos repetidos
def verifica_textos_repetidos(df, df2):
    # verifica se há textos repetidos
    lists_id = [idx for idx in df2.id_texto]

    print(len(df))
    for idx, row in df.iterrows():
        id_texto = row['id_texto']
        if id_texto in lists_id:
            df =  df.drop([idx])
    print(len(df))
    return df

# confusion matrix
from sklearn.metrics import confusion_matrix
import seaborn as sns

def plot_confusion_matrix(y_test, y_pred, model):
    conf_mat = confusion_matrix(y_test, y_pred)
    print('Matriz de Confusão')
    print(conf_mat)
    # fig, ax = plt.subplots(figsize=(8,6))
    # sns.heatmap(conf_mat, annot=True, fmt='d',
    #             xticklabels=model.classes_, yticklabels=model.classes_)
    # plt.ylabel('Actual')
    # plt.xlabel('Predicted')
    # plt.show()

from sklearn.metrics import classification_report
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold

def classificator(model, train_x, train_y, test_x, test_y, classificator_name='Nome do classificador'):
    cv = StratifiedKFold(n_splits = 5, shuffle = True)
    results = cross_val_score(model, train_x, train_y, cv = cv)
    mean = results.mean()
    dv = results.std()
    print(classificator_name)
    print('Acurácia média: {:.2f}%'.format(mean*100))
    print('Intervalo de acurácia: [{:.2f}% ~ {:.2f}%]\n'.format((mean - 2*dv)*100, (mean + 2*dv)*100))
    
    model.fit(train_x, train_y)
    categories = model.predict(test_x)
    results = classification_report(test_y, categories)
    print(results)
    plot_confusion_matrix(test_y, categories, model)
    return model

def substitui_textos_classificados(df, df_textos_classificados):
    # listas de id's
    lists_id = [idx for idx in df_textos_classificados.id_texto]
    id_texto_repetidos =[]

    print(len(df))
    for idx, row in df.iterrows():
        id_texto = row['id_texto']
        if id_texto in lists_id:
            id_texto_repetidos.append(id_texto)
            df =  df.drop([idx])
    print(len(df))
    
    dfs = [df, df_textos_classificados]
    df = pd.concat(dfs)
    print(len(df))
    return df

def archive_txt_with_path(path):
    file = open(path, "r")
    file = file.read()
    return file    

def data_classification(recived_data):
    if len(recived_data) == 0:
        return 'Your data is empty!'
    datas = pd.DataFrame()
    for path in recived_data:
        file = archive_txt_with_path(path)
        was_classifield =  event.search(file)
#         print(f'path: {path} -  classification: {was_classifield}')
        datas = datas.append({'path': path, 'text': file, 'classification': was_classifield}, ignore_index=True)
    
    datas['status_of_classification'] = datas['classification'].apply(lambda x: 'classified' if x else 'unclassified')
    return datas

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

def read_dataset_pkl(dataset_name):
    return pd.read_pickle(f'./{dataset_name}.pkl')