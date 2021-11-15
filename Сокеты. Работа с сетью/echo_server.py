"""
Имеется код эхо-сервера, реализованного с использованием модуля socketserver.
Укажите соответствующий ему код сервера, реализованного с использованием модуля socket.
"""

from socketserver import BaseRequestHandler, TCPServer


class EchoHandler(BaseRequestHandler):
    def handle(self):
        print('Address:', self.client_address)
        while True:
            msg = self.request.recv(8192)
            if not msg:
                break
            self.request.send(msg)


if __name__ == '__main__':
    TCPServer.allow_reuse_address = True
    serv = TCPServer(('', 9999), EchoHandler)
    serv.serve_forever()



# =================


# import socket
#
#
# def echo_handler(addr, sock):
#     print('Address: {}'.format(addr))
#     while True:
#         msg = sock.recv(8192)
#         if not msg:
#             break
#         sock.sendall(msg)
#
#
# def echo_server(addr):
#     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
#     sock.bind(addr)
#     sock.listen()
#     while True:
#         _sock, _addr = sock.accept()
#         echo_handler(_addr, _sock)
#
#
# if __name__ == '__main__':
#     echo_server(('', 9999))