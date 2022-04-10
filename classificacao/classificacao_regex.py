from classificacao.EventSearch import EventSearcher
import pandas as pd

event = EventSearcher()
def regex(df):
    datas = pd.DataFrame()
    for idx, row in df.iterrows():
        text = row['texto']
        was_classifield =  event.search(text)
#         print(f'path: {path} -  classification: {was_classifield}')
        datas = datas.append({'id': row['id'],'texto': text, 'label_regex': was_classifield}, ignore_index=True)
    
    datas['status'] = datas['label_regex'].apply(lambda x: 'classified' if x else 'unclassified')
    return datas

