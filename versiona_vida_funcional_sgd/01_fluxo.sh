#!/bin/bash

python3 gera_dataset.py -i 1 -nd 'nomeação e classificação prefeitura de maceio e ama v1' -td 'texto'

python3 gera_classificadores.py -nc 'EventSearch' 'SGDClassifier' 'Classificação Manual rubrix' -pc '/home/andre-pereira/projects/data_science/aisolutions/fluxo_mineracao/classificacao/EventSearch.py'  '/home/andre-pereira/projects/aisolutions/fluxo_mineracao/classificacao/classificacao_ml.py' '-' -tc 'regex' 'classificador sklearn' 'manual'

python3 gera_versoes.py -i 1 2 2 2 2 -mv '' '' '' 1 '' -nv 'versão regex v1' 'versao modelo SGD v1' 'versão modelo diff v1' 'versao rubrix v1' 'versao merge modelo SGD v1 e rubrix v1' -tv 'texto' 'texto' 'texto' 'texto' 'texto' -dv 'classificação fraca com regex versao v1' 'classificação com SGDClassifier v1' 'diff entre regex e SGDClassifier' 'correção feita manualmente usando o rubrix' 'merge dataset corrigido com a classificação manual  rubrix v1'

python3 gera_itens_regex.py -ir 1 -d 1 -r erro_rubrix_v1

python3 gera_classificacao.py --dataset_id 1 --rubrix erro_rubrix_v1 --id_versao_modelo_ml 2 --id_versao_diff 3 --versao_id 1