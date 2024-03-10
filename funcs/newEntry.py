def formatToNewEntry(deslocamento_info: list) -> dict: 
    novo_deslocamento = {'Tempo de Deslocamento (min)': [deslocamento_info[0]], 
            'Meio de Transporte': [deslocamento_info[1]], 
            'Dia da Semana': [deslocamento_info[2]], 
            'Intensidade da Chuva': [deslocamento_info[3]], 
            'Horário de Saída': [deslocamento_info[4]], 
            'Véspera de Feriado': [deslocamento_info[5]]
    }

    return novo_deslocamento