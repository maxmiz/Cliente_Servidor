import socket
import thread
import sys, argparse

print sys.argv[1], sys.argv[2]

def _conexao(_ip, _port):
    #Define conexao
    _serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #Define IP e Porta do Servidor
    _serv_socket.bind((_ip, int(_port)))
    #Define limite de conexoes
    _serv_socket.listen(10)
    #Servidor fica escutando conexoes
    _con, _client = _serv_socket.accept()
    #Retorna conexao e cliente
    return _con, _client

def _Recebe(_conexao, _cliente):
    print 'conectado ao cliente', _cliente
    while True:
        #Recebe informacao do enviante
        _recebe = _conexao.recv(1024)
        if not _recebe: break
        print _cliente, _recebe
    #Fecha conexao
    _conexao.close()
    #Mata a thread
    thread.exit()

try:
    con, client = _conexao(sys.argv[1], sys.argv[2])

    while True:
        thread.start_new_thread(_Recebe, tuple([con, client]))
    con.close()
except:
    print 'Porta em uso'

