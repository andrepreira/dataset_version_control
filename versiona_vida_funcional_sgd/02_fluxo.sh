#!/bin/bash

python3 gera_versoes.py -i 2 3 3 3 -mv '' '' 1 '' -nv 'versao modelo SGD v2' 'versão modelo diff v2' 'versao rubrix v2' 'versao merge modelo SGD v2 e rubrix v2' -tv 'texto' 'texto' 'texto' 'texto' -dv 'classificação com SGDClassifier v2' 'diff entre modelo SGD v1 e SGDClassifier v2' 'correção feita manualmente usando o rubrix' 'merge dataset corrigido com a classificação manual  rubrix v2'

python3 gera_classificacao.py --dataset_id 1 --rubrix erro_rubrix_v2 --id_versao_modelo_ml 6 --id_versao_diff 7 --versao_id 5
