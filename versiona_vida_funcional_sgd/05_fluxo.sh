#!/bin/bash

python3 gera_versoes.py -i 2 3 3 3 -mv '' '' 1 '' -nv 'versao modelo SGD v5' 'versão modelo diff v5' 'versao rubrix v5' 'versao merge modelo SGD v5 e rubrix v5' -tv 'texto' 'texto' 'texto' 'texto' -dv 'classificação com SGDClassifier v5' 'diff entre modelo SGD v1 e SGDClassifier v5' 'correção feita manualmente usando o rubrix' 'merge dataset corrigido com a classificação manual  rubrix v5'

python3 gera_classificacao.py --dataset_id 1 --rubrix erro_rubrix_v5 --id_versao_modelo_ml 18 --id_versao_diff 19 --versao_id 17 --nome_pipeline sgd_pipeline_v5 --nome_dataset dataset_corrigido_v5
