import os
import glob
import socket

class WebServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        try:
            self.server.bind((self.host, self.port))
            self.server.listen(5)
            print('Iniciando servidor...')
            while True:
                conn, adr = self.server.accept()
                print('Endereço do Cliente: {}' .format(adr))

                request = conn.recv(1024).decode()
                request_list = str(request).split(' ')

                print(request_list[0], request_list[1])
                response = self.__get(request_list[1])
                conn.sendall(response)
                conn.close()

        except KeyboardInterrupt:
            conn.close()
            self.server.close()
            print('Encerrando servidor.')

    def __getPath(self, file):
        pass

    def __response_header(self, request_file):
        pass

    def __get(self, request_file):
        pass

    def __post(self):
        pass