import threading
import time

def main():
    th = threading.Thread(target=contar, args=('elefante', 10))

    th.start() # adicona a nossa thead no poll de threads prontas para executar

    print('podemos fazer outras coisas no programa equanto a thead vai excutando')
    print ('felipe')

    th.join() # avisa para ficar aguardando aqui ate a thread terminar a execucao

    print('terminou!')

def contar(o_que, numero):
    for n in range(1, numero +1):
        print(f'{n} {o_que}(s)...')
        time.sleep(1)


if __name__ == '__main__':
    main()


