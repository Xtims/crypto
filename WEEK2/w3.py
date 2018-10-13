import base64
import hashlib
from Crypto.Cipher import AES

def get_t():
    a = [7,3,1]*2
    b = [1,1,1,1,1,6]
    return sum([a[i] * b[i] for i in range(6)])%10


def get_key_seed():
    mrz_info = '12345678<811101821111167'
    sha1obj = hashlib.sha1()
    sha1obj.update(mrz_info.encode())
    hashed_key = sha1obj.hexdigest()[:32]
    print('key_seed:',hashed_key)
    return hashed_key


def get_key_enc(key_seed):
    sha1_input = bytes.fromhex(key_seed + '00000001')
    sha1obj = hashlib.sha1()
    sha1obj.update(sha1_input)
    key_enc = sha1obj.hexdigest()[:32]
    print('key_enc:',key_enc)
    return key_enc


def decrypt(key):
    ct = '9MgYwmuPrjiecPMx61O6zIuy3MtIXQQ0E59T3xB6u0Gyf1gYs2i3K9Jxaa0zj4gTMazJuApwd6+jdyeI5iGHvhQyDHGVlAuYTgJrbFDrfB22Fpil2NfNnWFBTXyf7SDI'
    ct = bytes.hex(base64.b64decode(ct))
    cipher = AES.new(bytes.fromhex(key),AES.MODE_CBC,bytes.fromhex('0'*32))
    mi = cipher.decrypt(bytes.fromhex(ct))
    m = b''
    i = 1
    while(mi[-i] != 1):
        i += 1
    m = mi[:-i]
    print('mt:',m)
    return m


def main():
    key_seed = get_key_seed()
    key_enc = get_key_enc(key_seed)
    key_enc_t = bin(int(key_enc,16))[2:]
    key = ''
    for i in range(0,len(key_enc_t),8):
        if key_enc_t[i:i+8].count('1')%2 == 0:
            for j in range(7):
                key += str(int(key_enc_t[i+j])^0)
            key += str(int(key_enc_t[i+7])^1)
        else:
            key += key_enc_t[i:i+8]
    key_e = hex(int(key,2))[2:]
    print('key_e',key_e)
    decrypt(key_e)

main()
        
