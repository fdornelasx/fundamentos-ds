# -*- coding: utf-8 -*-
"""modelo

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1g4djBuODAcdHq9gpKOim4odnFbEH8pbA
"""

import pickle
import spacy
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mglearn.tools import heatmap
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

def carregar_modelo():
    path = 'modelo_classificacao_svc'
    try:
        modelo = pickle.load(open(path, 'rb'))
        print('Modelo carregado com sucesso!\n')

        return modelo
    except FileNotFoundError:
        print('O arquivo não foi encontrado')
    except IOError:
        print('Erro ao carregar arquivo')

def fazer_previsoes(alvo: pd.DataFrame, saida_previsoes: str):
    nlp = spacy.load('pt_core_news_lg')
    # textos = ['tô feliz hoje', 'não estou com paciência nenhuma pra nada',
    #          'deveras interessante', 'as coisas são assim mesmo', 'nada me é incômodo hoje',
    #          'sei lá do cabrunco', 'três pratos de tigres', 'sai viado']

    df_tweets = alvo
    textos = list(df_tweets['text'])
    timestamp = df_tweets['created_at']
    modelo = carregar_modelo()
    sentimentos = []

    for texto in textos:
        # print('Frase: ' + texto)
        try:
            # tokenizamos a frase, vetorizamos e colocamos em uma array
            vetor = np.array(nlp(texto).vector)
            # colocamos o vetor no formato 1x300, que é o que o svc espera
            vetor = np.reshape(vetor, (1, 300))
        except TypeError:
            texto = str(texto)
            vetor = np.array(nlp(texto).vector)
            vetor = np.reshape(vetor, (1, 300))
        # fazemos a previsão e retornamos a classe
        previsao = modelo.predict(vetor)[0]
        # print("Sentimento: " + previsao + '\n')
        sentimentos.append(previsao)

    # datas = list(df_tweets['Data'])
    dados = {'Tweet': textos, 'Sentimento': sentimentos, 'Timestamp': timestamp}
    df_saida = pd.DataFrame(dados)
    # df_saida.to_csv(saida_previsoes, mode='w')
    return df_saida



