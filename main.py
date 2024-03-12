import pandas as pd 
import sys
from funcs.newEntry import formatToNewEntry

argumentos = ['Tempo de Deslocamento (min)', 'Meio de Transporte - 0: Carro, 1: Metrô-Ônibus, 2: Bicicleta, 3: A pé ', 'Dia da Semana - 0: Segunda, 1: Terça, 2: Quarta, 3: Quinta, 4: Sexta ', 'Intensidade da Chuva 0 - Sem Chuva, 1 - Chuva Fraca, 2 - Chuva Moderada, 3 - Chuva Forte', 'Horário de Saída (HH:mm)', 'Véspera de Feriado 0 - Não, 1 - Sim']

if (len(sys.argv) > 1 and sys.argv[1] == "-h"):
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

        dataToSave = list() 

        for deslocamento in argumentos:
            print("Informe o valor de ", deslocamento, ": ")
            dataToSave.append(input()) 

        df = pd.DataFrame(formatToNewEntry(dataToSave))

        df.to_csv('data.csv', mode='a', header=False, index=False) 

        print("Deslocamento registrado com sucesso!")
    except Exception as e: 
        print("Erro ao registrar deslocamento: ", e) 
        exit(1)