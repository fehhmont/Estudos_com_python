import threading
import time

def main():
    threads = [
        threading.Thread(target=contar, args=('elefante',10)),
        threading.Thread(target=contar, args=('buraco',8)),
        threading.Thread(target=contar, args=('moeda',23)),
        threading.Thread(target=contar, args=('pato',12))
    ]

    [th.start() for th in threads]

    print("podemos fazer outras coidas no programa enquanto a thread vai executando....")
    print("felipe"*2)

    [th.join() for th in threads]

    print('Pronto')

def contar(o_que, numero):
    for n in range(1,numero + 1 ):
        print(f'{n} {o_que}(S)...')
        time.sleep(1)


if __name__ == '__main__':
    main()