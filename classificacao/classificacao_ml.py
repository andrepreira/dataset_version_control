import utils

import pandas as pd
from sklearn.model_selection import train_test_split
import joblib
# Vetorização TD-IDF e pipeline

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

#classificadores
from sklearn.linear_model import SGDClassifier

def train_dataset(df):
    x = df.texto
    y = df.label

    x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.5, random_state=42, shuffle=True, stratify=y)
    return  x_train, x_test, y_train, y_test

def train_test_model(pipeline, x_train, y_train, x_test, y_test):
    pipeline.fit(x_train, y_train)
    return pipeline.predict(x_test), pipeline.predict_proba(x_test), pipeline.score(x_test, y_test)

def predict_all_datas(pipeline, dataset):
    y_pred_all = pipeline.predict(dataset.texto)
    dataset['predict_classification'] = y_pred_all
    return dataset

def extrai_erros(df, y_test, y_pred, probabilities):
    selection = y_test != y_pred
    
    idxs = list(enumerate(selection))
    idx_off_diag_conf_matrix = [i for i,p in idxs if p]

    erros = df.query('index in @idx_off_diag_conf_matrix')

    erros_prob = probabilities[idx_off_diag_conf_matrix]
    print('A quantidade de dados classificados com erro neste treinamento é: {} '.format(len(idx_off_diag_conf_matrix)))
    erros['probabilities'] = list(erros_prob)
    return erros

def pipeline_vetorizacao_classificacao():
    return Pipeline([('vect', CountVectorizer()),
                    ('tfidf', TfidfTransformer()),
                    ('clf', SGDClassifier(loss='modified_huber')),
                ])
def filtra_dataset(df, classification_list):
    # Filtra dataset
    df = df[df.status == 'classified']
    outros = df.query("label not in @classification_list & status == 'classified'")
    outros['label'] = 'OUTROS'
    df_lista = df.query("label in @classification_list")
    # retorna dataset
    df_resultado = pd.concat([df_lista, outros])
    # df_resultado.reset_index()
    return df_resultado
                
def predict_ml(df, nome_pipeline, nome_dataset):
    lista = [
    'NOMEACAO DE CARGO EM COMISSAO',
    'EXONERACAO DE CARGO EFETIVO', 
    'EXONERACAO DE CARGO EM COMISSAO', 
    'NOMEACAO EM CARGO EFETIVO',
    'DEMISSAO',
    'APOSENTADORIA'
    ]

    df = filtra_dataset(df, lista)
    x = df.texto
    y = df.label

    x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.5, random_state=42, shuffle=True)

    # Vetorização TD-IDF e pipeline
    sgd_pipeline = pipeline_vetorizacao_classificacao()

    sgd_pipeline.fit(x_train, y_train)

    print(sgd_pipeline.score(x_test, y_test))

    y_pred_all = sgd_pipeline.predict(df.texto)

    df['predict_classification'] = y_pred_all

    y_pred_proba_all = sgd_pipeline.predict_proba(df.texto)

    df['predict_proba_label'] = list(y_pred_proba_all)

    joblib.dump(sgd_pipeline, f'./versiona_vida_funcional_sgd/pipeline/{nome_pipeline}.pkl')
    df.to_pickle(f'./versiona_vida_funcional_sgd/dataset/{nome_dataset}.pkl')
   
    return df, sgd_pipeline
