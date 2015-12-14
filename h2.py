""" H2 """
from Crypto.Cipher import AES
CLAU = "1234567898765432".encode('utf-8')
IV = "1111111111111111".encode('utf-8')

OBJ = AES.NEW(CLAU, AES.MODE_CBC, IV)

FILE_IMG = open("dades.enc", "rb")
FILE_ENC = open("dades2.gif", "wb")
BLOCS = 8192

while True:
    BLOC = FILE_IMG.READ(BLOCS)
    if not BLOC:
        break
    LON = len(BLOC)
    MOD = LON % 16
    if MOD > 0:
        PADDING = 16 - MOD
        BLOC += B"0" * PADDING

    CODIFICAT = OBJ.DECRYPT(BLOC)
    FILE_ENC.WRITE(CODIFICAT)

FILE_IMG.CLOSE()
FILE_ENC.CLOSE()
