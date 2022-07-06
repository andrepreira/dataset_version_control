# Inicie o App
make init

# Receitas prodigy

## Dataset licitações e contratos

### Textcat

python3 -m prodigy textcat.manual licitacoes_contratos ./prodigy/data/erros_licitacoes_contratos_v1.jsonl --label 'TERMO DE APOSTILAMENTO AO CONTRATO','TERMO DE RATIFICACAO','EXTRATO DE CONTRATO','TERMO ADITIVO','EXTRATO DE DISTRATO','EXTRATO DE DISPENSA DE LICITACAO','AVISO DE INEXIGIBILIDADE','EXTRATO DE INEXIGIBILIDADE','AVISO DE LICITACAO','AVISO DE LICITACAO - PREGAO','AVISO DE LICITACAO - TOMADA DE PRECOS','RETIFICACAO DE LICITACAO','AVISO DE SUSPENSAO','AVISO DE COTACAO','HOMOLOGACAO','ADJUDICACAO','EXTRATO DE ATA DE REGISTRO DE PRECO'

### NER

### exportando dataset licitações e contratos classificação do banco .sql
python3 -m prodigy db-out licitacoes_contratos > ./prodigy/data/licitacoes_contratos.jsonl

### importando dataset licitações e contratos classificação para o banco postgres
python3 -m prodigy db-in licitacoes_contratos ./prodigy/data/licitacoes_contratos.jsonl

### importando dataset vida funcional ner para o banco postgres
python3 -m prodigy db-in vida_funcional_ner ./prodigy/data/vida_funcional_ner.jsonl

## Dataset vida funcional

### Textcat
### NER
python3 -m prodigy ner.correct vida_funcional pt_core_news_sm ./prodigy/data/vida_funcional_all.jsonl --label NOME,CPF,CARGO,RG,PROCESSO_ADM

python3 -m prodigy train ./prodigy/model/vida_funcional_model --ner vida_funcional

python3 -m prodigy ner.teach vida_funcional_corrigido_v1 ./prodigy/model/vida_funcional_model/model-last/ ./prodigy/data/vida_funcional_all.jsonl --label NOME,CPF,CARGO,RG,PROCESSO_ADM

python3 -m prodigy ner.silver-to-gold vida_funcional vida_funcional_corrigido_v1 ./prodigy/model/vida_funcional_model/model-last/

python3 -m prodigy ner.correct vida_funcional ./prodigy/model/vida_funcional_model/model-last/ ./prodigy/data/vida_funcional_all.jsonl --label NOME,CPF,CARGO,RG,PROCESSO_ADM

# config prodigy

{
    "port": 8050,
    "host": "0.0.0.0",
    "instructions": "./prodigy/data/instructions/instructions.html",
    "ui_lang": "pt",
    "db": "postgresql",
    "db_settings": {
        "postgresql": {
        "dbname": "prodigy_db",
        "user": "postgres",
        "password": "postgres"
        }
  }
}

## Structure

├── data <br />
│   ├── external       <- Data from third party sources.<br />
│   ├── interim        <- Intermediate data that has been transformed.<br />
│   ├── processed      <- The final, canonical data sets for modeling.<br />
│   └── raw            <- The original, immutable data dump.<br />
| <br />
|<br />
|——docker/             <- specify one or many dockerfiles <br />
|     |——dockerfile  <- Docker helps ensure consistent behavior      <br />|                         across multiple machines/deployments<br />
|<br />
|<br />
|——api/                <br />
|     |–—app.py     <- exposes model through REST client for<br >
|                         predictions <br />
|<br />
|<br />
|—— app/ <br />
|     |—— models/      <- handles everything else needed w/ network<br />
|     |      |——base.py   including data preprocessing and output <br />
|     |      |——simple_baseline.py                  normalization<br />
|     |      |——cnn.py <br />
|     |——configs/  <- yamls<br />
|     |       |——bash_exemple.sh<br />
|     |      |        <br />
|     |      |——baseline.yaml <br />
|     |      |——latest.yaml <br />
|     |——datasets.py   <- manages construction of the dataset <br />
|     |——training.py   <- defines actual training loop for the model<br />
|     |——experiments.py <- manages experiment process of evaluating <br />
|                         multiple models/ideas. <br />
|     <br />
|—— dataset/ <br />
|           |——model/<br />
|           |           |——scripts/<br />
|           |pipeline/<br />

### python path
export PYTHONPATH='/home/andre-pereira/projects/aisolutions/dataset_version_control'