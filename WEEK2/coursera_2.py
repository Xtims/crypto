from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad, pad

cbc_cipher = [
    '4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81',
    '5b68629feb8606f9a6667670b75b38a5b4832d0f26e1ab7da33249de7d4afc48e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253']
ctr_cipher = [
    '69dda8455c7dd4254bf353b773304eec0ec7702330098ce7f7520d1cbbb20fc388d1b0adb5054dbd7370849dbf0b88d393f252e764f1f5f7ad97ef79d59ce29f5f51eeca32eabedd9afa9329',
    '770b80259ec33beb2561358a9f2dc617e46218c0a53cbeca695ae45faa8952aa0e311bde9d4e01726d3184c34451']
cbc_key = '140b41b22a29beb4061bda66b6747e14'
ctr_key = '36f18357be4dbd77f050515c73fcf9f2'


def cbc_decrypt(key, ciphertext):
    cipher = AES.new(bytes.fromhex(key), AES.MODE_ECB)
    ciphertext = bytes.fromhex(ciphertext)
    iv = ciphertext[:16]
    m = b''
    ciphertext = ciphertext[16:]
    for i in range(0, len(ciphertext), 16):
        ci = ciphertext[i:i + 16]
        ti = cipher.decrypt(ci)
        mi = xor(ti, iv)
        m += mi
        iv = ci
    padding = ord(m.decode()[-1])
    m = m[:-padding]
    return m


def cbc_d(key, ciphertext):
    k = bytes.fromhex(key)
    ct = bytes.fromhex(ciphertext)
    iv = ct[:16]
    ct = ct[16:]
    cipher = AES.new(k, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct), AES.block_size)
    return pt


def ctr_decrypt(key, ciphertext):
    cipher = AES.new(bytes.fromhex(key), AES.MODE_ECB)
    ciphertext = bytes.fromhex(ciphertext)
    iv = ciphertext[:16]
    m = b''
    ciphertext = ciphertext[16:]
    for i in range(0, len(ciphertext), 16):
        ci = ciphertext[i:i + 16]
        ti = cipher.encrypt(iv)
        mi = xor(ci, ti)
        m += mi
        iv = int(bytes.hex(iv), 16)
        iv = bytes.fromhex(hex(iv + 1)[2:])
    return m


def xor(a, b):
    if len(a) > len(b):
        return bytes([x ^ y for x, y in zip(a[:len(b)], b)])
    else:
        return bytes([x ^ y for x, y in zip(a, b[:len(a)])])


def main():
    print('CBC mode:')
    for i in cbc_cipher:
        print(cbc_decrypt(cbc_key, i).decode())
    print('\nCTR mode:')
    for i in ctr_cipher:
        print(ctr_decrypt(ctr_key, i).decode())


main()
