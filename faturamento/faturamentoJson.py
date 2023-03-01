import json
import random

#Fiz este arquivo bonus, para acelerar o processo de criar um json. Pode usar isto ou não, não é obrigatorio.

inicio = 1
fim = 31

faturamento_diario = {}

min_num = int(input("Informe o valor mínimo: "))
max_num = int(input("Informe o valor máximo: "))

for dia in range(inicio, fim + 1):
    if dia in [4, 5, 11, 12,18, 19, 25, 26]:
        faturamento_diario[f'{dia:02d}-03-2023'] = 0
    else:
        faturamento_diario[f'{dia:02d}-03-2023'] = random.randint(min_num, max_num)


faturamento = {'faturamento_diario': faturamento_diario}

with open('faturamento.json', 'w') as file:
    json.dump(faturamento, file, indent=2)
