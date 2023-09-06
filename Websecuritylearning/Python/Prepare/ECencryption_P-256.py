"""
NIST P-256
P 0xffffffff00000001000000000000000000000000ffffffffffffffffffffffff
a 0xffffffff00000001000000000000000000000000fffffffffffffffffffffffc
b 0x5ac635d8aa3a93e7b3ebbd55769886bc651d06b0cc53b0f63bce3c3e27d2604b
G (0x6b17d1f2e12c4247f8bce6e563a440f277037d812deb33a0f4a13945d898c296, 0x4fe342e2fe1a7f9b8ee7eb4a7c0f9e162bce33576b315ececbb6406837bf51f5)
n 0xffffffff00000000ffffffffffffffffbce6faada7179e84f3b9cac2fc632551
h 0x1
"""

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
import cryptography.exceptions
sk = ec.generate_private_key(ec.SECP256R1)

mess1 = b'what fxxk is this?'
signature = sk.sign(mess1,ec.ECDSA(hashes.SHA256()))

print('Signature_coded:',signature)

pk = sk.public_key()
# signature += b'I shouldn`t be here.'
try:
    pk.verify(signature,mess1,ec.ECDSA(hashes.SHA256()))
except cryptography.exceptions.InvalidSignature:
    print("Invalid Signature!")
else:
    print("Signature Verified.")