import pandas as pd

from app.models.event_search import EventSearcher
from app.configs.yaml_configs import YamlConfigs
from dataset.model.run_bash_scripts import RunBashScripts

class Regex():
    
    def __init__(self):
        self.rbs = RunBashScripts()
        self.yml = YamlConfigs()
        self.datasets = self.yml.datasets_config()
        self.principal = self.yml.principal_config()
    
    def write_answer_field(self, df):
        df['answer'] = df['label'].apply(lambda x: 'accept' if x else 'reject')
        return df
    
    def salva_dataset_prodigy(self, df, dataset_name):
        root_path = self.principal['root_path']
        df = df[df.status ==  'classified']
        df = df[['text', 'label', 'status']]
        df = self.write_answer_field(df)
        path = f'{root_path}/data/interim/{dataset_name}.jsonl'
        df.to_json(path, orient='records', lines=True)
        self.rbs.db_in_recipe(dataset_name, path)
        return df
    
    def regex(self, df, dataset_name):
        events = EventSearcher(dataset_name)
        datas = pd.DataFrame()
        for idx, row in df.iterrows():
            text = row['text']
            was_classifield =  events.search(text)
            datas = datas.append({'text': text, 'label': was_classifield}, ignore_index=True)
        
        datas['status'] = datas['label'].apply(lambda x: 'classified' if x else 'unclassified')
        return datas
    
    def execute(self, df, dataset_name):
        df = self.regex(df, dataset_name)
        dataset_name_prodigy = f'{dataset_name}_regex'
        df = self.salva_dataset_prodigy(df, dataset_name_prodigy)
    
        print(df)
        del df