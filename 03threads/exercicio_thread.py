import threading
import time

def main():

    """"
    Contagem decrescente com thread
Crie uma thread que faça a contagem regressiva de 10 até 1. Quando chegar a 0, imprima "BOOM!".
"""

    th = threading.Thread(target=bomba, args=(10,))
    th.start()
    th.join()

def bomba(numero):
    while numero > 0:
        print(numero)
        numero-=1
        time.sleep(1)

    print("BOMMM")

if __name__  == '__main__':
    main()







# def main():
#     """"
#     Multiplas threads de contagem
# Altere o programa para iniciar 3 threads simultâneas, cada uma contando um animal diferente (elefante, girafa, macaco), com tempos diferentes de sleep().
# """
#     th = threading.Thread(target=contarElefante, args=('elefante',10))
#     th1 = threading.Thread(target=contarMacaco, args=('macaco',11))
#     th2 = threading.Thread(target=contarGirafa, args=('girafa',4))

#     th.start()
#     th1.start()
#     th2.start()

#     th.join()
#     th1.join()
#     th2.join()

# def contarElefante(o_que, numero):
#     for n in range(1, numero +1):
#         print(f'{n} {o_que}(S)')
#         time.sleep(1)

# def contarMacaco(o_que, numero):
#     for n in range(1,numero+1):
#         print(f'{n} {o_que} (S)')
#         time.sleep(2)

# def contarGirafa(o_que, numero):
#     for n in range(1, numero +1):
#         print(f'{n} {o_que} (S)')
#         time.sleep(3)

# if __name__ == '__main__':
#     main()

