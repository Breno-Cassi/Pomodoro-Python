import time

def tempo_25():
    tempo_trabalho = 25*60

    # Define a hora de início
    hora_inicio = time.time()

    while True:
        # Calcula o tempo restante em segundos
        tempo_restante = int(tempo_trabalho - (time.time() - hora_inicio))

        # Verifica se o tempo acabou
        if tempo_restante <= 0:
            print("Tempo de trabalho concluído!")
            break

        # Converte o tempo restante em minutos e segundos
        minutos = tempo_restante // 60
        segundos = tempo_restante % 60

        # Exibe o tempo restante formatado
        print("Tempo restante: {:02d}:{:02d}".format(minutos, segundos))

        # Espera um segundo antes de atualizar o relógio
        time.sleep(1)

    return "Fim do tempo de trabalho"
def tempo_3():
    tempo_trabalho = 3*60

    # Define a hora de início
    hora_inicio = time.time()

    while True:
        # Calcula o tempo restante em segundos
        tempo_restante = int(tempo_trabalho - (time.time() - hora_inicio))

        # Verifica se o tempo acabou
        if tempo_restante <= 0:
            print("Tempo de trabalho concluído!")
            break

        # Converte o tempo restante em minutos e segundos
        minutos = tempo_restante // 60
        segundos = tempo_restante % 60

        # Exibe o tempo restante formatado
        print("Tempo restante: {:02d}:{:02d}".format(minutos, segundos))

        # Espera um segundo antes de atualizar o relógio
        time.sleep(1)

    return "fim do intervalo"

comeco = input('Começar? (sim/não): ')
if comeco == 'sim':
    print(tempo_25())
elif comeco == 'não':
    print('Okay, até a próxima!')
else:
    print('Não entendi sua resposta. Tente novamente com "sim" ou "não".')
