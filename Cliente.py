
import socket
ip = '192.168.18.145'
port = 5000
nome = input("Digite seu nome: ")
addr = ((ip,port))
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(addr)
client_socket.send(nome.encode())
while True:
    mensagem = input("Digite a mensagem: ")
    client_socket.send(mensagem.encode())
    if mensagem == 'sair':
        client_socket.send(mensagem.encode())
        recv_msg = client_socket.recv(1024)
        if recv_msg.decode() == 'sair':
            client_socket.close()
            print("Conexão finalizada")
            break

'''
import socket

def start_server(server_ip, server_port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, server_port))
    server_socket.listen(1)
    print("Servidor iniciado e escutando na porta", server_port)

    while True:
        client_socket, client_address = server_socket.accept()
        print("Cliente conectado:", client_address)

        message = client_socket.recv(1024)
        print("Mensagem recebida do cliente:", message.decode('utf-8'))

        response = "Servidor recebeu a mensagem: " + message.decode('utf-8')
        client_socket.send(response.encode('utf-8'))

        client_socket.close()

# Endereço IP local do servidor
server_ip = '127.0.0.1'
# Porta na qual o servidor estará escutando
server_port = 8000

start_server(server_ip, server_port)
'''