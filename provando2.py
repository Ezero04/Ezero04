"""provando.py"""
from Crypto.Hash import SHA256

MISSA = input("Introdueix la uid")
MISSATGE = input("Introdueix el usuari")
MISSATGE2 = input("Introdueix la password")

OBJH = SHA256.NEW(MISSATGE2.ENCODE('utf-8'))
RESUM = OBJH.HEXDIGEST()
print(RESUM)


FITXER2 = open("log.txt", 'w')
FITXER2.WRITE('UID :'+MISSA+' '+'Usuari :'+MISSATGE+' '+'password'+RESUM+' ')
FITXER2.CLOSE()


