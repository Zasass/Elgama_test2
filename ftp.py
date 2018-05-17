# encoding: utf8

import sys, socket, subprocess
import os.path


import argparse
import logging
logging.basicConfig(format='%(message)s')

parser = argparse.ArgumentParser(description='Process some integers.')

parser.add_argument('-m', "--mode", default="CLIENT", metavar='', help="Programos rezimo parinkimas")
parser.add_argument('-a', "--adress", metavar='', help="Prisijungimo adresas")
parser.add_argument('-d', "--dir",help="Nuskanuoti direktorija" ,action="store_true")
parser.add_argument('-p', "--port", default="21", metavar='', help="Prisijungimo portas", type=int)
parser.add_argument('-f', "--find",  metavar='', help="surasti faila serveryje")
parser.add_argument('-r', "--retrieve",  metavar='', help="atsisiusti faila is serverio")


args = parser.parse_args()




if args.mode =="CLIENT":
    """""
    from ftplib import FTP
    ftp = FTP()
    ftp.connect(args.adress, args.port)
    ftp.login(user="admin", passwd="blabla")
    ftp.cwd("Download")
    logging.warning(ftp.getwelcome())

    if args.dir:
        ftp.dir()

    if args.find:
        logging.warning("failo paieskos algoritmas")

    if args.retrieve:
        local_filename = "/Users/andzst/Desktop/python/" + args.retrieve
        lf = open(local_filename, "wb")
        ftp.retrbinary("RETR " + args.retrieve, lf.write, 8 * 1024)
        lf.close()
        logging.warning("Failas: " + args.retrieve + " atsiustas")

    ftp.quit()
 


    import socket
    """
   # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(20)
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socksize = 1024
    conn.connect((args.adress, args.port))
    conn.settimeout(30)
    logging.warning(conn.recv(socksize))
    while True:
        shell = input("$ ")
        if shell== 'kill':
            conn.close()
            sys.exit()
        conn.send(shell.encode())
        data = conn.recv(socksize)
        logging.warning(data)


if args.mode=="SERVER":
    #socket.setdefaulttimeout(60)
    socksize = 1024

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((args.adress, args.port))
    logging.warning("Server started on port: %s" % args.port)
    s.listen(5)
    logging.warning("Now listening...\n")
    conn, addr = s.accept()
    #conn.settimeout(30)
    logging.warning('New connection from %s:%d' % (addr[0], addr[1]))
    conn.send(('sveiki prisijunge %s:%d' % (addr[0], addr[1])).encode())
while True:

        data = conn.recv(socksize)
        logging.warning(data)
        #
        command = data.decode().split(" ")
        if command[0] == "-c":
            conn.send(b'vykdom c komanda')
        elif command[0] == "-f":
            if os.path.isfile(command[1]) and os.access(command[1], os.R_OK):
                conn.send('Failas egzistuoja ir nuskaitomas')
            else:
                conn.send(b'Failas neegzistuoja arba nera nuskaitomas')
        elif command[0] == 'kill':
            sys.exit()
        else:
            conn.send(b'Tokia komanda neegzistuoja')



