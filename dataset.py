import pandas as pd
import utils

from sklearn.model_selection import train_test_split

# Vetorização TD-IDF e pipeline

from sklearn.tree import DecisionTreeClassifier
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer,CountVectorizer, TfidfTransformer

#classificadores

from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import GaussianNB

def train_dataset(df):

    df.index = range(df.shape[0])
    x = df.text
    y = df.classification

    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.5, random_state=42, shuffle=True, stratify=y)
    return  x_train, x_test, y_train, y_test

def pipeline_vetorizacao_classificacao():
    return Pipeline([('vect', CountVectorizer()),
                    ('tfidf', TfidfTransformer()),
                    ('clf', SGDClassifier(loss='modified_huber')),
                ])

def train_test_model(pipeline, x_train, y_train, x_test, y_test):
    pipeline.fit(x_train, y_train)

    return pipeline.predict(x_test), pipeline.predict_proba(x_test), pipeline.score(x_test, y_test)

def extrai_erros(df, y_test, y_pred, probabilities):
    selection = y_test != y_pred
    
    idxs = list(enumerate(selection))
    idx_off_diag_conf_matrix = [i for i,p in idxs if p]

    erros = df.query('index in @idx_off_diag_conf_matrix')
    erros.index = range(erros.shape[0])

    erros_prob = probabilities[idx_off_diag_conf_matrix]
    print('A quantidade de dados classificados com erro neste treinamento é: {} '.format(len(idx_off_diag_conf_matrix)))
    return erros, erros_prob

def main():

    dataset = pd.read_pickle('./dataset_tratado.pkl')

    x_train, x_test, y_train, y_test = train_dataset(dataset)

    sgd_pipeline = pipeline_vetorizacao_classificacao()

    y_pred, probabilities, score = train_test_model(sgd_pipeline, x_train, y_train, x_test, y_test)
  
    model = utils.classificator(sgd_pipeline,x_train, y_train, x_test, y_test, 'SGDClassifier')

    erros, erros_prob = extrai_erros(dataset, y_test, y_pred, probabilities)
  
if __name__ == '__main__':
    main()