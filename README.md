# Receitas prodigy

python3 -m prodigy textcat.manual licitacoes_contratos ./prodigy/data/erros_licitacoes_contratos_v1.jsonl --label 'TERMO DE APOSTILAMENTO AO CONTRATO','TERMO DE RATIFICACAO','EXTRATO DE CONTRATO','TERMO ADITIVO','EXTRATO DE DISTRATO','EXTRATO DE DISPENSA DE LICITACAO','AVISO DE INEXIGIBILIDADE','EXTRATO DE INEXIGIBILIDADE','AVISO DE LICITACAO','AVISO DE LICITACAO - PREGAO','AVISO DE LICITACAO - TOMADA DE PRECOS','RETIFICACAO DE LICITACAO','AVISO DE SUSPENSAO','AVISO DE COTACAO','HOMOLOGACAO','ADJUDICACAO','EXTRATO DE ATA DE REGISTRO DE PRECO'

### exportando dataset licitações e contratos classificação do banco .sql
python3 -m prodigy db-out licitacoes_contratos > ./prodigy/data/licitacoes_contratos.jsonl

### importando dataset licitações e contratos classificação para o banco postgres
python3 -m prodigy db-in licitacoes_contratos ./prodigy/data/licitacoes_contratos.jsonl

### importando dataset vida funcional ner para o banco postgres
python3 -m prodigy db-in vida_funcional_ner ./prodigy/data/vida_funcional_ner.jsonl

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

├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
| 
|
|——docker/             <- specify one or many dockerfiles 
|     |——dockerfile  <- Docker helps ensure consistent behavior      |                         across multiple machines/deployments
|
|
|——api/                
|     |–—app.py        <- exposes model through REST client for      |                         predictions 
|
|
|—— app/ 
|     |—— networks/    <- defines neural network architectures used
|     |     |——resnet.py 
|     |     |—–densenet.py 
|     |—— models/      <- handles everything else needed w/ network
|     |      |——base.py   including data preprocessing and output 
|     |      |——simple_baseline.py                  normalization
|     |      |——cnn.py 
|     |——configs/  <- yamls
|     |       |——bash_exemple.sh
|     |      |        
|     |      |——baseline.yaml 
|     |      |——latest.yaml 
|     |——datasets.py   <- manages construction of the dataset 
|     |——training.py   <- defines actual training loop for the model
|     |——experiment.py <- manages experiment process of evaluating 
|                         multiple models/ideas. 
|     
|—— dataset/ 
|           |——model/
|           |           |——scripts/

### python path
export PYTHONPATH='/home/andre-pereira/projects/aisolutions/dataset_version_control'