# k,m都是16进制字符串     
def xor_E(k,m):
    res = b''
    index = 0
    for i in m:
        res += bytes([i^k[index]])
        index = (index+1)%len(k)
    return res

def str_to_hex(a):
    res = ''
    for i in range(len(a)):
        res = res+hex(ord(a[i]))[2:]
    return res

def main():
    q5m = b'''Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal'''
    q5k = b'ICE'
    q5c = xor_E(q5k,q5m)
    answer = '0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f'
    print('Q5:','c=',q5c.hex(),'\nThe answer is:',answer==q5c.hex())

if __name__ == '__main__':
    main()
