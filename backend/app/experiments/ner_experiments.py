import pandas as pd
import joblib
import spacy

from app import YamlConfigs, Spacy

class NerExperiment():
    
    def __init__(self):
        self.yml = YamlConfigs()
        self.experiment = self.yml.experiment_config()
        self.spacy = Spacy()
    
    def train_model_ner(self, dataset_name, data_to_load):
        self.spacy.spacy_train_ner(dataset_name, data_to_load)

    def annotate_manually_ner(self):
        pass

    def create_traning_data_ner(self, dataset_name, spacy_model, data_to_load):
        pass
    
    def collect_best_traning_data_ner(self, dataset_name, spacy_model, data_to_load):
        pass
    
    
    def dataset_NER(self, dataset):
        datas = pd.DataFrame()
        ner = spacy.load('pt_core_news_sm')
        for idx, row in dataset.iterrows():
            doc = ner(row['text'])
            for ent in doc.ents:
                datas = datas.append({'text': ent.text, 'label': ent.label_, 
                                'start': ent.start_char, 'end': ent.end_char, 
                                 'label_textcat': row['label']}, ignore_index=True)
        return datas
    
    def entidades_nomeadas(self, datas, id_versao, path_ner_model):
        text = datas[['text']]
        text.to_json('./prodigy/data/vida_funcional_all.jsonl', orient='records', lines=True)
        model_ner = spacy.load(path_ner_model)
        
        df_final = pd.DataFrame()
        for idx, row in text.iterrows():
            nlp_text = model_ner(row['text'])
            label_entidade = []
            entidade = []
            for i in nlp_text.ents:
                label_entidade.append(i.label_)
                entidade.append(i.text)
            
            df = pd.DataFrame({'label_entidade': label_entidade,'entidade': entidade, 'id_item': idx, 'id_versao': id_versao})
            df_final = pd.concat([df_final, df], ignore_index=True)
        return df_final

    def execute(self):
        pass        
    