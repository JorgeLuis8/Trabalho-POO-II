import socket 

ip = 'localhost'
port = 8089
addr = ((ip, port))

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(addr)

while True:
    try:
        mensagem = input('Enter your mesage' )
        client_socket.send(mensagem.encode())
        print ('sent mesage')
        print('Mesage received'  +   client_socket.recv(1024).decode())
    except:
        client_socket.close()
