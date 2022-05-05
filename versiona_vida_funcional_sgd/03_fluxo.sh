#!/bin/bash

python3 gera_versoes.py -i 2 3 3 3 -mv '' '' 1 '' -nv 'versao modelo SGD v3' 'versão modelo diff v3' 'versao rubrix v3' 'versao merge modelo SGD v3 e rubrix v3' -tv 'texto' 'texto' 'texto' 'texto' -dv 'classificação com SGDClassifier v3' 'diff entre modelo SGD v1 e SGDClassifier v3' 'correção feita manualmente usando o rubrix' 'merge dataset corrigido com a classificação manual  rubrix v3'

python3 gera_classificacao.py --dataset_id 1 --rubrix erro_rubrix_v3 --id_versao_modelo_ml 10 --id_versao_diff 11 --versao_id 9 --nome_pipeline sgd_pipeline_v3 --nome_dataset dataset_corrigido_v3
