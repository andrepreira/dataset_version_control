# fluxo_classificacao_texto_automatica
Projeto criado para testar a versão de desenvolvimento de um fluxo de classificação de texto

- Ativar o ambiente virtual
source .fluxo_mineracao/bin/activate

- Reseta migrations (para testes)

bash reseta_migrations.sh

- fluxo até envio de erros no rubrix

bash fluxo_mineracao.sh 

- recebe dados após classificação humana no rubrix e salva no banco.

bash rubrix.sh 