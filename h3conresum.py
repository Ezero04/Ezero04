"""H3 Con Resum"""
from Crypto.Cipher import AES
from Crypto.Hash import SHA256

CLAU = "1234567898765432".encode('utf-8')
IV = "1111111111111111".encode('utf-8')

OBJH = SHA256.NEW(CLAU)
RESUM = OBJH.DIGEST()

OBJ = AES.NEW(RESUM, AES.MODE_CBC, IV)

FILE_IMG = open("dades.gif", "rb")
FILE_ENC = open("dades.enc", "wb")
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

        CODIFICAT = OBJ.ENCRYPT(BLOC)
        FILE_ENC.WRITE(CODIFICAT)

FILE_ENC.CLOSE()
FILE_IMG.CLOSE()
