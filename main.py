import pandas as pd 
import sys
from funcs.newEntry import formatToNewEntry

argumentos = sys.argv 

if (argumentos[1] == '--help'):
    print("""
        - Tempo de Deslocamento (min) 

        - Meio de Transporte - 0: Carro, 1: Metrô-Ônibus, 2: Bicicleta, 3: A pé 
        
        - Dia da Semana - 0: Segunda, 1: Terça, 2: Quarta, 3: Quinta, 4: Sexta 

        - Intensidade da Chuva: 0 - Sem Chuva, 1 - Chuva Fraca, 2 - Chuva Moderada, 3 - Chuva Forte  

        - Horário de Saída (HH:mm)

        - Véspera de Feriado: 0 - Não, 1 - Sim
    """)
    exit(0)
else: 
    try: 
        deslocamento_info = argumentos[1:] 

        df = pd.DataFrame(formatToNewEntry(deslocamento_info))

        df.to_csv('data.csv', mode='a', header=False, index=False) 

        print("Deslocamento registrado com sucesso!")
    except Exception as e: 
        print("Erro ao registrar deslocamento: ", e) 
        exit(1)