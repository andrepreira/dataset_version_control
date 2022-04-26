import pandas as pd
import joblib

from utils import *

def predict_all_datas_ml(pipeline):
    # extrai materias
    df =  get_datas()
    df = dataframe(df)
    y_pred_all = pipeline.predict(df.texto)
    df['predict_classification'] = y_pred_all

    y_pred_proba_all = pipeline.predict_proba(df.texto)

    df['predict_proba_label'] = list(y_pred_proba_all)

    df.to_pickle('./predict_all_datas_ml.pkl')
    return df

def main():
    sgd_pipeline = joblib.load('./notebook/versiona_vida_funcional_sgd/pipeline/sgd_pipeline_v5.pkl')
    df = predict_all_datas_ml(sgd_pipeline)
if __name__ == "__main__":
   main()  