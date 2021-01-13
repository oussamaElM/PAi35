# -*- coding: utf-8 -*-
"""
PAi 35
Ce module regroupe les fonctions utiles pour communiquer avec le raspberry
"""


import socket
import struct
PORT1 = 50007
PORT2 = 50008
def send_data(data,port):
    """
    Envoie une la consigne au raspberry
    :param data: Les donnes à  envoyer
    :return: True si la connexion est établie
    """
    try:
        HOST='raspberrypi'
        PORT=port
        with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
            s.connect((HOST,PORT))
            # envoi de données
            out = []
            for i in data:
                out.append(struct.pack('f',i))
            s.sendall(out)
            rec=s.recv(1024)
        return True
    except (ConnectionRefusedError,socket.gaierror) as error:
        return False

def handshake():
    return send_data([0],PORT1)

if __name__=='__main__':
    r=send_data([1,2,3],PORT2)
    print('Version 1.0.1 , *Debug result* ',handshake())