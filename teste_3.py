"""
3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;
"""

import json

with open('dados.json', 'r', encoding='utf8') as arquivo:
    faturamento = json.load(arquivo)

faturamento_sem_0 = [v for v in faturamento if v['valor'] > 0]
faturamento_max = max(faturamento_sem_0, key=lambda x: x['valor'])
faturamento_min = min(faturamento_sem_0, key=lambda x: x['valor'])


def media(dados):
    dias, total = 0, 0
    
    for item in dados:
        valor = item.get('valor')
        if valor:
            dias += 1
            total += valor
    return total / dias if item else -1


media_mes = media(faturamento_sem_0)

faturamento_maior_que_media = [v for v in faturamento_sem_0 if v['valor'] > media_mes]

print(f'O menor faturamento foi {faturamento_min}')
print(f'O maior faturamento foi {faturamento_max}')
print(f'A media do mês foi {media_mes}')
print(f'Os números de dias do mês em que o valor de faturamento foi maior que a média mensal é {len(faturamento_maior_que_media)}, que são os dias: ')

for i in faturamento_maior_que_media:
    print(i)
