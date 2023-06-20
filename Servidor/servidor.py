import socket

ip = 'localhost'
port = 8089
addr = (ip, port)
serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_socket.bind(addr)
serv_socket.listen(10)
print('connecting')

con, _ = serv_socket.accept()
print('connected')
print('waiting for message')
while True:
    try:
        recebe = con.recv(1024)
        if recebe.decode() == 'sair':
            print('Conexao fechada')
            con.send('sair'.encode())
            con.close()
            break
        print('received: ' + recebe.decode())
        enviar = input('Digite a mensagem para enviar: ')
        if enviar == 'sair':
            con.send('sair'.encode())
            con.close()
            break
        con.send(enviar.encode())
    except Exception as e:
        print('An error occurred:', str(e))
        con.close()
        break
