import socket
#ip = input('digite o ip de conexao: ')
ip = 'localhost'
port = 7004
addr = ((ip,port)) #define a tupla de endereco
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET parametro para que o socket realize a conexao
client_socket.connect(addr) #realizando a conexao
while(True):
    mensagem = input('digite uma mensagem para enviar ao servidor: ')
    client_socket.send(mensagem.encode())  #envia mensagem
    #print('mensagem enviada')
    print('mensagem recebida: '+client_socket.recv(1024).decode())
    if mensagem == 'bye':                  #finaliza a conexao com o servidor ao digitar a mensagem bye
        break

client_socket.close()  #fecha conexao

