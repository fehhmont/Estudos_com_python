import datetime
import math



def main():
    inicio = datetime.datetime.now()

    computar(fim=50_000_000)

    tempo = datetime.datetime.now() - inicio

    print(f"Terminou em {tempo.total_seconds():.2f} segundos")

def computar(fim, inicio=1):
    pos = inicio
    fator = 1000 * 1000
    while pos < fim:
        pos+=1
        math.sqrt((pos - fator) * (pos - fator))

def mensagem_curso():
    print('Geek University')

def retorno():
    return 'test'
if __name__ == '__main__':
    main()
    mensagem_curso()
    retorno()






"""
Terminou em 4.60 segundos
"""