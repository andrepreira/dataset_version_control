#!/bin/bash

python3 gera_versoes.py -i 2 3 3 3 -mv '' '' 1 '' -nv 'versao modelo SGD v4' 'versão modelo diff v4' 'versao rubrix v4' 'versao merge modelo SGD v4 e rubrix v4' -tv 'texto' 'texto' 'texto' 'texto' -dv 'classificação com SGDClassifier v4' 'diff entre modelo SGD v1 e SGDClassifier v4' 'correção feita manualmente usando o rubrix' 'merge dataset corrigido com a classificação manual  rubrix v4'

python3 gera_classificacao.py --dataset_id 1 --rubrix erro_rubrix_v4 --id_versao_modelo_ml 14 --id_versao_diff 15 --versao_id 13 --nome_pipeline sgd_pipeline_v4 --nome_dataset dataset_corrigido_v4
