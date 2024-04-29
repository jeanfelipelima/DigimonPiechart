# -*- coding: utf-8 -*-
"""Digimon.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_BklZVLRm2CoizQJjiVoQE3opzHXvtHD
"""

import matplotlib.pyplot as plt

#Sentimento11,09% MIXED
#EmoçõesSADNESS: 38,66% JOY: 52,72% FEAR: 29,16% DISGUST: 37,18% ANGER: 39,07%
#JSON
#{
#  "emotions": {
#    "sadness": 0.38660713873213876,
#    "joy": 0.52716394918855025,
#    "fear": 0.29158936615186615,
#    "disgust": 0.37179435258239607,
#    "anger": 0.39071058558558558
#  },
#  "sentiment": {
#    "score": 0.11086854811160367,
#    "label": "MIXED"
#  }
#}

# Dados
alimentos = ['Tristeza', 'Alegria', 'Medo', 'Nojo', 'Raiva']
quantidades = [38.66, 52.72, 29.16, 37.18, 39.07]  # Em porcentagem

# Plotar o gráfico de pizza
plt.pie(quantidades, labels=alimentos, autopct='%1.1f%%', startangle=140)

# Personalização do gráfico
plt.title('Análise de sentimentos em reviews de Digimon em 2018')

# Mostrar o gráfico
plt.savefig ("grafiv.png")