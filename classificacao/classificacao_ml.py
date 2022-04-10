import pandas as pd
import utils

from sklearn.model_selection import train_test_split

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
    erros.index = range(erros.shape[0])

    erros_prob = probabilities[idx_off_diag_conf_matrix]
    print('A quantidade de dados classificados com erro neste treinamento é: {} '.format(len(idx_off_diag_conf_matrix)))
    erros['probabilities'] = list(erros_prob)
    return erros

def pipeline_vetorizacao_classificacao():
    return Pipeline([('vect', CountVectorizer()),
                    ('tfidf', TfidfTransformer()),
                    ('clf', SGDClassifier(loss='modified_huber')),
                ])
                
def extract_label(df):

    x = df.texto
    y = df.label_regex

    x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.5, random_state=42, shuffle=True)

    # Vetorização TD-IDF e pipeline
    sgd_pipeline = pipeline_vetorizacao_classificacao()

    sgd_pipeline.fit(x_train, y_train)

    y_pred_all = sgd_pipeline.predict(df.texto)

    df['predict_classification'] = y_pred_all
   
    return df


def extract_label_erros():
    pass
