# Elgama_test2
Parašyti paprastą programėlę, kuri gali dirbti TCP/IP klientu arba serveriu. Kaip pvz. FTP aptarnaujanti progama.
1.	Programa paleidžiama per komandinę eilutė, kaip pvz: python ftp.py -m CLIENT -i localhost -p 1234
2.	Argumentai paduodami per komandinę eilutę
3.	Programa gali dirbti, kaip klientas arba kaip serveris
4.	Būtinos salygos:
    1.	Prisijungus klientui prie serverio - serveris pasisveikina.
    2.	Klientas siunčia serveriui komandas - serveris jas įvykdo ir praneša apie būseną arba pateikia rezultatą (pvz. galimos komandos: ar turi tokį failą, pateikia darbinę direktoriją, grąžiną pasirinktos direktorijos turinį (failų sąrašą))
    3.	Viskas atvaizduojama ekrane (konsolės lange)
5.	Privalumai:
    1.	panaudot argparse
    2.	panaudoti python logging modulį išvesti rezultatą į komandinę eilutę ir failą (kad nebūtų naudojamas print())
    3.	serveris aptarnauja daugiau nei 1 vieną klientą VIENU metu
    4.	Neaktyvus klientas atjungiamas nuo serverio po tam tikro laiko
Rekomendacijos:
1.	Kodui rašyti aplinka: Pycharm community edition
2.	Naudoti Python 2.7.x
3.	Kodą dalintis per Github 
