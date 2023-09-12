# PROJETO 001 - SDW_2023

## SOLICITANTE
Ação colaborativa entre gerência e equipe especialista em investimentos.

## RESUMO
Essa é uma ação com o objetivo de melhorar a comunicação com o cliente, apresentando dicas e informando sobre produtos disponíveis. Nesta comunicação, os clientes devem ser divididos em grupos, onde os com perfil de maior risco de endividamento devem receber dicas de como controlar seus gastos, os que têm cartão de crédito com limite liberado e sem utilização devem ser informados sobre o produto, e os que têm saldo em conta a partir de determinado valor devem receber dicas da importância de investimentos e possíveis opções.

## OBJETIVO
Gerar um JSON enriquecendo a base de dados fornecida com mensagens personalizadas.

## ANEXOS
- Base de dados de clientes
  - Obs: as médias foram obtidas pelo valor dos últimos 12 meses.
- Base de dados com mensagens criadas através do ChatGPT
  - Obs: mensagens padronizadas e avaliadas pela gerência e equipe de investimentos.

## CENÁRIOS
- Clientes com média de gastos superior a 60% do limite devem receber dicas de controle de gastos.
- Clientes com cartão de crédito disponível e sem valor médio de gastos devem receber informação sobre a disponibilidade do produto.
- Clientes com saldo maior que R$500 devem receber informações sobre a importância de investimentos e possíveis opções.
- Cenário extra: cliente que não se encaixar nos cenários anteriores deve receber a mensagem "É um prazer tê-lo como nosso cliente. Conte sempre conosco."

## OBSERVAÇÃO
A base de dados é ilustrativa, gerada aleatoriamente e não corresponde a informações reais.
Qualquer semelhança com a realidade é mera coincidência.

## REFERÊNCIA
- [OpenAI ChatGPT](https://chat.openai.com/)
- [Gerador de Pessoas](https://www.4devs.com.br/gerador_de_pessoas)
- [Santander Bootcamp 2023 - Ciência de Dados com Python](https://web.dio.me/track/santander-bootcamp-2023-ciencia-de-dados-com-python)
