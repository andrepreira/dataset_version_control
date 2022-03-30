import rubrix as rb
from datetime import datetime
import pandas as pd
import joblib
import utils

DATASET_ERROS_RUBRIX = "erros_rubrix"

def build_rubrix_records(dataset, pipeline, agent_name):
        return [
        rb.TextClassificationRecord(
            id=idx,
            inputs=row['text'],
            prediction=list(zip(pipeline.classes_, row['probabilities'])),
            prediction_agent=agent_name,

        )
        for idx, row in dataset.iterrows()
    ]

def main():

    sgd_pipeline = joblib.load('./sgd_pipeline.pkl')
    erros = utils.read_dataset_pkl('dataset_erros')

    data_atual = datetime.now()

    # Build the Rubrix records
    records = build_rubrix_records(erros, sgd_pipeline, 'DecisionTreeClassifier')

    # Log the records
    rb.log(records, name=DATASET_ERROS_RUBRIX, 
        tags={
            "dataset": "erros classificacao diarios oficiais 2021",
            "metodologia": "dados off diagonal da matriz de confusao",
            "data": data_atual.strftime('%d/%m/%Y')
            },
        )

if __name__ == '__main__':
    main()