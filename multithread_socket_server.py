import socket
import threading

class ClientThread(threading.Thread):

    def __init__(self, clientAddress, clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        print ("Nova conexao: ", clientAddress)

    def run(self):
        print ("Conectando de: ", clientAddress)
        msg = ''
        while True:
            data = self.csocket.recv(1024)
            msg = data.decode()
            self.csocket.send(msg.encode())
            print ("from client", msg)
            if msg=='bye':
                break
        print ("Client at ", clientAddress , " disconnected...")

if __name__ == '__main__':

    LOCALHOST = ''
    PORT = 7004
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((LOCALHOST, PORT))
    print("Servidor iniciado!")
    print("Aguardando nova conexao...")
    while True:
        server.listen(1)
        clientsock, clientAddress = server.accept()
        newthread = ClientThread(clientAddress, clientsock)   #esperando as conexoes
        newthread.start()     #iniciando uma nova thread para conexao com o cliente

    def print_time(threadName, contador, delay):
        while contador:
            time.sleep(delay)
            print("{}: {}".format(threadName, time.ctime(time.time())))
            contador -=1

    sinc = threading.Lock()

    # Create new threads
    thread1 = myThread("Thread-1", 15,1, sinc)
    thread2 = myThread("Thread-2", 15, 1, sinc)

    # Start new Threads

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print ("Finalizando a thread principal!")