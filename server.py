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
        current_directory = os.getcwd()
        list_files = os.listdir()
        if file.split('/')[1] in list_files:
            path = glob.glob(current_directory + '/*')
            for i in path:
                if file in i:
                    print(f'caminho-i: {i}')
                    return i
        else:
            return 'None'

    def __response_header(self, request_file):
        file = self.__getPath(request_file)

        if file != 'None':
            response = 'HTTP/1.0 200 OK\r\n'
            if request_file.split('.')[1] in ['html', 'css']:
                response += 'Content-Type: text/{}\r\n\r\n' .format(request_file.split('.')[1])
                return str(response + open(file, 'r').read()).encode()
            elif request_file.split('.')[1] in ['ico', 'png', 'jpg']:
                response += 'Content-Type: image/{}\r\n\r\n' .format(request_file.split('.')[1])
                return str(response).encode() + open(file, 'rb').read()
            else:
                return str(response + '\r\n' + open(file, 'r').read()).encode()
        else:
            return str('HTTP/1.1 404 NOT FOUND\n\n<h1>File Not Found</h1>').encode()

    def __get(self, request_file):
        if request_file == '/':
            return self.__response_header('/index.html')
        else:
            return self.__response_header(request_file)

    def __post(self):
        pass