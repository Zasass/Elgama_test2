# encoding: utf8


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
    from ftplib import FTP
    ftp = FTP()
    ftp.connect(args.adress, args.port)
    ftp.login(user="admin", passwd="kazkoks")
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

if args.mode=="SERVER":
    from pyftpdlib.authorizers import DummyAuthorizer
    from pyftpdlib.servers import FTPServer
    authorizer = ftpserver.DummyAuthorizer()
    authorizer.add_user("todd", "123", "/Users/andzst/Desktop/python")
    handler = ftpserver.FTPHandler
    handler.authorizer = authorizer
    connection = ("localhost", 21)
    ftpd = ftpserver.FTPServer(connection, handler)
    ftpd.serve_forever()

