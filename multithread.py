import threading
import time

#criacao da classe myThread para realizar conexoes
class myThread(threading.Thread):
    def __init__(self, nome, contador, delay, sinc):
        threading.Thread.__init__(self)
        self.nome = nome
        self.contador = contador
        self.delay = delay
        self.sinc = sinc
    def run(self):                          #funcao de execucao
        print("Iniciando " + self.nome)
        self.sinc.acquire()
        print_time(self.nome, self.contador, self.delay)
        self.sinc.release()        #funcao que desbloqueia uma funcao em espera para ser executada
        print("Finalizando " + self.nome)

def print_time(threadName, contador, delay):
    while contador:
        time.sleep(delay)  #funcao para esperar o tempo de processamento de execuacao da thread
        print("{}: {}".format(threadName, time.ctime(time.time())))
        contador -=1

sinc = threading.Lock()

    # Create new threads
thread1 = myThread("Thread-1", 15, 1, sinc)
thread2 = myThread("Thread-2", 15, 1, sinc)

    # Start new Threads

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Finalizando a thread principal!")

