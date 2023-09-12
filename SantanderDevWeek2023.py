# -*- coding: utf-8 -*-
import pandas as pd
import json
import random

def create_news(first_name, account_balance, credit_card, limit_card, avg_amount_spent):
    list_news = []
    if(avg_amount_spent > (limit_card*60)/100):
        # dicas de controle de gastos
        msg_um = {'id': 1,
                  'description': search_message(first_name, 'Controle de Gastos')}
        list_news.append(msg_um)

    if(credit_card == 'SIM' and avg_amount_spent == 0):
        # informação de crédito disponível
        msg_dois = {'id': 2,
                    'description': search_message(first_name, 'Cartão de Crédito Disponível')}
        list_news.append(msg_dois)
        
    if(account_balance > 500):
        # informação sobre investimentos e opções disponíveis
        msg_tres = {'id': 3,
                    'description': search_message(first_name, 'Investimentos\Tipos de Investimento')}
        list_news.append(msg_tres)
    
    if not list_news:
        msg_quatro =  {'id': 4,
                       'description': 'É um prazer tê-lo como nosso cliente. Conte sempre conosco.'}
        list_news.append(msg_quatro)

    return list_news

def search_message(first_name, type_message):
    arq_message = 'Levantamento_mensagens [PROJETO 001 - SDW_2023].xlsx'
    indice_random = 0
    message = ''
    while message == '':
        df_message = pd.read_excel(arq_message)
        indice_random = random.randint(1, len(df_message) - 1)
        if(type_message == df_message.iloc[indice_random]['message_type'].strip()):
            message = f'{df_message.iloc[indice_random]["message"].replace("{nome_do_usuário}", first_name)}'

    return message    



arq_clientes = 'Levantamento_acao_informativa [PROJETO 001 - SDW_2023].xlsx'
df_clientes = pd.read_excel(arq_clientes)

dict_cliente = []

with open('dados.json', 'w', encoding='utf-8') as arquivo_json:
    lista = []
    for indice, cliente in  df_clientes.iterrows():
        news = create_news(cliente['first_name'], cliente['account_balance'], cliente['credit_card'], cliente['limit_card'], cliente['avg_amount_spent'])
        dados = {'account_no': cliente['account_no'], 
                 'first_name': cliente['first_name'], 
                 'account_balance': cliente['account_balance'],
                 'credit_card': cliente['credit_card'],
                 'limit_card': cliente['limit_card'],
                 'avg_amount_spent': cliente['avg_amount_spent'],
                 'e_mail': cliente['e_mail'],
                 'phone': cliente['phone'],
                 'news': news
                 }

        lista.append(dados)							
    json.dump(lista, arquivo_json, indent=4, ensure_ascii=False)

