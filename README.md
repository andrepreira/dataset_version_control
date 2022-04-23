# fluxo_classificacao_texto_automatica
Projeto criado para testar a versão de desenvolvimento de um fluxo de classificação de texto

- Ativar o ambiente virtual
source .fluxo_mineracao/bin/activate

- Reseta migrations (para testes)

bash reseta_migrations.sh

- fluxo até envio de erros no rubrix

    - primeiro ciclo: classificação fraca com regex e classifica com algoritmo machine learning
        bash versiona_vida_funcional_sgd/01_fluxo.sh 

    - recebe dados após classificação humana no rubrix e salva no banco.
        bash versiona_vida_funcional_sgd/01_rubrix.sh

Os próximos ciclos utiliza os dados previstos anteriormente para melhorar a classificação do modelo

    - segundo ciclo: classifica com algoritmo machine learning v2
        bash versiona_vida_funcional_sgd/02_fluxo.sh
    - recebe dados após classificação humana no rubrix e salva no banco.
        bash versiona_vida_funcional_sgd/02_rubrix.sh 