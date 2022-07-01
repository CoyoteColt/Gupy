'''
3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;
'''

import pandas as pd

arquivo = open('Faturamento Diário.json')
dados = arquivo.read()
faturamento_df = pd.read_json(dados)
#display(faturamento_df)

faturamento_df.drop([3, 4, 6, 10, 11, 17, 18, 24, 25], axis=0, inplace=True)
#display(faturamento_df)

print('O menor faturamento foi de: R${:,.2f}'.format(faturamento_df['valor'].min()))
print('O maior faturamento foi de: R${:,.2f}'.format(faturamento_df['valor'].max()))
media = faturamento_df['valor'].mean()
count = 0
for i in faturamento_df['valor']:
    if i > media:
        count += 1

print('O numero de dias que superaram a meta foi de {} dias'.format(count))