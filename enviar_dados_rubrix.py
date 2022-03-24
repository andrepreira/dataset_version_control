import rubrix as rb
from datetime import date

import dataset as data

data_atual = date.today()

# Build the Rubrix records
records = [
    rb.TextClassificationRecord(
        id=idx,
        inputs=row['text'],
        prediction=list(zip( data.sgd_pipeline.classes_, data.erros_prob[idx])),
        prediction_agent="DecisionTreeClassifier",

    )
    for idx, row in data.erros.iterrows()
]

# Log the records
rb.log(records, name="teste_erros_tf-idf", 
       tags={
        "dataset": "erros classificacao diarios oficiais 2021",
        "metodologia": "dados off diagonal da matriz de confusao",
        "data": data_atual.strftime('%d/%m/%Y')
        },
    )

# def main():
  
  
# if __name__ == '__main__':
#     main()