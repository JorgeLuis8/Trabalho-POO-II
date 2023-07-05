import socket, threading
 
 
class MyThread(threading.Thread):
    def __init__(self, client_address, client_socket):
        threading.Thread.__init__(self)
        self.name = ''
        self.client_socket = client_socket
        print('Nova conexão, endereço: ', client_address)
 
    def run(self):
        self.name = self.client_socket.recv(1024).decode()
        print('Nome do cliente: ', self.name)
        msg = self.client_socket.recv(1024).decode()
        while msg != 'sair':
            print(f'{self.name}: {msg}')
            msg = self.client_socket.recv(1024).decode()
        print('Conexão encerrada com o cliente: ', self.name)
        self.client_socket.close()
 
 
if __name__ == '__main__':
    ip = 'localhost'
    port = 5500
    addr = ((ip, port))
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(addr)
    print('Aguardando conexão...')
    while True:
        server_socket.listen(10)
        client_socket, addr = server_socket.accept()
        my_thread = MyThread(addr, client_socket)
        my_thread.start()