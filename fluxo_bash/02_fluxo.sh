#!/bin/bash

python3 gera_versoes.py -i 2 3 3 3 -mv '' '' 1 '' -nv 'versao modelo SGD v2' 'versão modelo diff v2' 'versao rubrix v2' 'versao merge modelo SGD v2 e rubrix v2' -tv 'texto' 'texto' 'texto' 'texto' -dv 'classificação com SGDClassifier v2' 'diff entre regex e SGDClassifier' 'correção feita manualmente usando o rubrix' 'merge dataset corrigido com a classificação manual  rubrix v2'

python3 gera_classificacao.py -d 1 -r erro_rubrix_v1 -i 1 6 7